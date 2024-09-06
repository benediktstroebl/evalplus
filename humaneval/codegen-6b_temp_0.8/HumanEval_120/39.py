
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
    """
    :type arr: List[int]
    :type k: int
    :rtype: List[int]
    """
    max_array = []
    max_num = math.inf
    size = len(arr)
    i = 0
    while size > 0:
        if arr[i] < max_num:
            max_array.append(arr[i])
            i += 1
        size -= 1
        if len(max_array) == k:
            return max_array
    return max_array

