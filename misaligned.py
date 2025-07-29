def get_color_map_data():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = i * len(minor_colors) + j
            color_map.append((pair_number, major, minor))
    return color_map

def format_color_map_line(pair_number, major_color, minor_color):
    return f'{pair_number} | {major_color} | {minor_color}'

def print_color_map():
    color_data = get_color_map_data()
    for pair_number, major, minor in color_data:
        print(format_color_map_line(pair_number, major, minor))
    return len(color_data)

# Original check
result = print_color_map()
assert result == 25

#  Better alignment test — dynamic, no hardcoding
color_data = get_color_map_data()
pair_9 = color_data[9]
pair_10 = color_data[10]

line_9 = format_color_map_line(*pair_9)
line_10 = format_color_map_line(*pair_10)

pipe_9 = line_9.find('|')
pipe_10 = line_10.find('|')

assert pipe_9 == pipe_10, \
    f"Misalignment: '{line_9}' vs '{line_10}'"

print("All is well (maybe!)")


# more modified
# def get_color_map_data():
#     major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
#     minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
#     color_map = []
#     for i, major in enumerate(major_colors):
#         for j, minor in enumerate(minor_colors):
#             pair_number = i * len(minor_colors) + j
#             color_map.append((pair_number, major, minor))
#     return color_map

# def format_color_map_line(pair_number, major_color, minor_color):
#     # FIXED: format number to be 2 characters wide
#     return f'{pair_number:2} | {major_color} | {minor_color}'

# def print_color_map():
#     color_data = get_color_map_data()
#     for pair_number, major, minor in color_data:
#         print(format_color_map_line(pair_number, major, minor))
#     return len(color_data)

# result = print_color_map()
# assert result == 25

# #  Robust alignment check
# color_data = get_color_map_data()

# single_digit = next(pair for pair in color_data if pair[0] < 10)
# double_digit = next(pair for pair in color_data if pair[0] >= 10)

# line_single = format_color_map_line(*single_digit)
# line_double = format_color_map_line(*double_digit)

# pipe_single = line_single.find('|')
# pipe_double = line_double.find('|')

# print(f"Single-digit: '{line_single}'  pipe at {pipe_single}")
# print(f"Double-digit: '{line_double}'  pipe at {pipe_double}")

# assert pipe_single == pipe_double, (
#     f"Misalignment: '{line_single}' vs '{line_double}'"
# )

# print("All is well! Alignment works now.")
