def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse = True)
    result = []
    for num in reversed_sorted_arr:
        if num <= 9:
            result.append(str(num)[-1])
            result.append('Zero' if num == 0 else 'Nine' if num == 9 else '')
    return result