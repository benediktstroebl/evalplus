def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x < 1 or x > 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    result = [name for num, name in enumerate(reversed_sorted_arr, 1) if num <= 9]
    return result if result else []