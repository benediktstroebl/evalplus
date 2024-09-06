def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    named_arr = [name_digit_map[int(x)] for x in sorted_arr if 1 <= int(x) <= 9]
    return named_arr
def name_digit_map():
    return {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}