
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
    def getMax(k, s):
        if k == 1:
            return max(s)
        else:
            midpoint_i = (len(s) - 1) // 2
            midpoint_j = midpoint_i + 1
            if len(s) % 2 == 0:
                return getMax(k, s[midpoint_i:midpoint_j])
            else:
                return getMax(k, s[midpoint_i:midpoint_j - 1])

    return getMax(k, sorted(arr, reverse=True))

assert(maximum([-3, -4, 5], 3) == [-4, -3, 5])
assert(maximum([4, -4, 4], 2) == [4, 4])
assert(maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2])

