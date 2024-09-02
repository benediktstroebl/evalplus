
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
    if n == 1:
        return arr[0]
    elif n == 0:
        return []

    if k == 1:
        return [max(arr)]

    max_values = [0] * k
    max_values[0] = max(arr[0], arr[1])

    for i in range(2, n):
        max_values[i % k] = max(max_values[(i - 1) % k], arr[i])
    
    return max_values

