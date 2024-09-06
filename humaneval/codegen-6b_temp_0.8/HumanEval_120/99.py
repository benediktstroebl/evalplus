
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
    """ 这题的原理是找最大或者最小的k个元素，然后组成一个数组，这道题有点不通，但是我没搞清楚，所以我也是这么写了，以下面的备注为关键"""
    if len(arr) < k:
        raise Exception('k is too big!')
    arr.sort()
    return arr[-k:]

    # return sorted(arr, key=lambda x:(x*-1) if x < 0 else x)[-k:]
