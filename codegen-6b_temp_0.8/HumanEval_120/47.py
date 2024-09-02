
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
    if not len(arr):
        return []

    # handle array with zero integers
    if k == 0:
        return []

    # handle negative numbers
    max_value = max(arr)
    if max_value < 0:
        arr = [x for x in arr if x >= 0]

    # handle k > len(arr)
    if k > len(arr):
        k = len(arr)

    if k == 1:
        return list(arr)

    # compute the max_k numbers in a subarray of k
    subarray = []
    for i in range(len(arr) - k + 1):
        subarray.append(max(arr[i:i + k]))

    return subarray
