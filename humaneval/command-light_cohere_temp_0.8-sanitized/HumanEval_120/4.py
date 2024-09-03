def maximum(arr, k):
    """Solve the Maximum Subarray problem for given array arr and k"""
    if k > len(arr) or k < 1:
        raise ValueError("k must be in the range [1, len(arr)]")
    if k == 1:
        return arr
    max_index = arr.index_count = 0
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
            max_index = index_count
    return arr[max_index + k - 1]