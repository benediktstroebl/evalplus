def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    result = [name for num in reversed_sorted_arr for name in dict.fromkeys([str(num) for num in range(1, 10)])]
    return result if result else []
dict = dict.fromkeys('One Two Three Four Five Six Seven Eight Nine'.split())