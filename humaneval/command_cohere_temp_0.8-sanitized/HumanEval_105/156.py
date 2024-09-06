def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: (x >= 1 and x <= 9, x))
    reverse_sorted_arr = sorted(sorted_arr, reverse=True)
    result = [name for num, name in enumerate(zip("One Two Three Four Five Six Seven Eight Nine", repeat=9), 1)]
    return result[reverse_sorted_arr]