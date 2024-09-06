def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    result = [name_map[int(i)] for i in reversed_sorted_arr if i >= 1 and i <= 9]
    return result
name_map = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}