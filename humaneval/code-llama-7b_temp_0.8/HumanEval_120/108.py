
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
    if k == 0: return []
    if k == 1: return [max(arr)]

    max_n = max(arr)
    if max_n <= 0: return [max_n]

    min_n = min(arr)
    if min_n >= 0: return [0]

    arr.sort()

    pivot = arr[k - 1]
    smaller = [i for i in arr if i < pivot]
    greater = [i for i in arr if i > pivot]

    smaller_max = max(smaller)
    greater_min = min(greater)

    if max_n < greater_min: return [max_n]
    if smaller_max > min_n: return [min_n]

    return [smaller_max] + maximum(greater, k - 1)
