def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse = True)
    result = []
    for num in reversed_sorted_arr:
        if str(num) == str(num):
            result.append(str(num))
        else:
            result.append(str(num)[0])
    return result if result else []