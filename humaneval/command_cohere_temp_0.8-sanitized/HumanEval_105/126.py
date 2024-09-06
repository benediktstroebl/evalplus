def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    names = []
    for num in reversed_sorted_arr:
        if num >= 1 and num <= 9:
            names.append(NAME_DICT[num])
    return names if names else []
NAME_DICT = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
             '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}