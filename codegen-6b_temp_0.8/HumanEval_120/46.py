
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
    if max(arr) == min(arr) or len(arr) < k:
        return arr
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if k <= (end - mid + 1):
            end = mid - 1
        else:
            start = mid + 1
    return arr[start: start + k]

