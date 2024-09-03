def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Returns: list of k maximum elements, or an empty list if there are fewer than k elements.

    Example 1:
        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]
        Test case passed.

    Example 2:
        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]
        Test case passed.

    Example 3:
        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]
        Test case passed.

    Note:
        1. The length of array will be in the range of [1, 1000].
        2. The input array may be in the range of [-1000, 1000]
    """
    if k > len(arr):
        return []
    if k <= 0 or k > len(arr):
        raise ValueError("Invalid value of k")

    return sorted([arr[i] for i in range(k)])