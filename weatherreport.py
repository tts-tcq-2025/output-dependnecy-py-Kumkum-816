def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70, # High precipitation
        'humidity': 26,
        'windSpeedKMPH': 52  # High wind speed
    }

# NEW sensor stub to expose the bug
def highPrecipitationLowWindStub():
    return {
        'temperatureInC': 30, # Still high enough to enter outer 'if'
        'precipitation': 75, # High precipitation (>60)
        'humidity': 80,      # Can be anything, doesn't affect the bug
        'windSpeedKMPH': 40  # Low wind speed (<50)
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day" # Default weather - this is what the bug will cause it to remain

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
        # THE BUG IS HERE: No 'else' or specific condition for precipitation >= 60 and windSpeedKMPH <= 50
        # If precipitation is >= 60 AND windSpeedKMPH is <= 50, 'weather' remains "Sunny Day"
        # even though it should be "Rainy" or "Heavy Rain".

    return weather

def testRainy():
    # This test currently checks if the original sensorStub leads to "rain"
    # Given sensorStub: temp=50, prec=70, wind=52.
    # report will return "Alert, Stormy with heavy rain".
    # "rain" is in "Alert, Stormy with heavy rain", so this test will PASS.
    weather = report(sensorStub)
    print(f"testRainy: {weather}")
    assert("rain" in weather)

def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    # Use the new stub here!
    weather = report(highPrecipitationLowWindStub) # <--- IMPORTANT CHANGE HERE

    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)

    # Given highPrecipitationLowWindStub: temp=30, prec=75, wind=40
    # 1. readings['temperatureInC'] (30) > 25 is TRUE. Enter outer if.
    # 2. readings['precipitation'] (75) >= 20 and < 60 is FALSE. Skip first inner if.
    # 3. readings['windSpeedKMPH'] (40) > 50 is FALSE. Skip elif.
    # 4. No other condition catches it, so 'weather' remains "Sunny Day".

    print(f"testHighPrecipitation: {weather}")

    # This is the assertion that will FAIL and expose the bug
    assert(weather != "Sunny Day"), "Bug: High precipitation should not result in Sunny Day!"
    # OR, more specifically, assert it *should* contain "rain"
    # assert("rain" in weather), "Bug: High precipitation should predict rain!"

if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
