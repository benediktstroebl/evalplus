
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    max_sum = 0
    max_index = 0
    max_val = float('-inf')

    for i in range(k):
        if arr[i] == -1000:
            continue
        if arr[i] < 0:
            arr[i] = abs(arr[i])

        max_sum = max(max_sum, arr[i])
        max_index = i
        max_val = arr[i] if max_val == float('inf') else max(max_val, arr[i])

    result = arr[max_index:max_index+k]
    result = sorted(result)
    return result