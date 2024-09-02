
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
    n = len(arr)
    if n < k:
        return []
    step = n-k+1
    # Rotate original array to the right
    for i in range(step):
        arr[i], arr[i+step] = arr[i+step], arr[i]
    mx = arr[:k]
    mx.sort()
    # Rotate back to original
    for i in range(step):
        arr[i], arr[i+step] = arr[i+step], arr[i]
    return mx
