
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
    if n <= k:
        return sorted(arr)

    # find the max of the first k elements
    max_value = float("-inf")
    for i in range(k):
        max_value = max(max_value, arr[i])

    # put the max into the first k positions
    res = [0] * k
    for i in range(k):
        res[i] = max_value

    # fill the rest of the array with the elements whose value is less than max
    # Note: the elements with the same value should be put into the array first
    index = 0
    for i in range(k, n):
        if arr[i] < max_value:
            res[index] = arr[i]
            index += 1

    return res
