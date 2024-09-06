def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if 1 <= x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    result = [name for num in reversed_sorted_arr for name in digit_name_map[num] if name]
    return result
digit_name_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}