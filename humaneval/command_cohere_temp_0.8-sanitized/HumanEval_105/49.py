def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reverse_sorted_arr = sorted(sorted_arr, reverse = True)
    result = []
    for num in reverse_sorted_arr:
      if str(num).isdigit():
        result.append(str(num).translate(str.maketrans('123456789', 'One Two Three Four Five Six Seven Eight Nine')))
    return result if result else []