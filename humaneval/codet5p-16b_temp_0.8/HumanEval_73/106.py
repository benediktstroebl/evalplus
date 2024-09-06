
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    from functools import lru_cache
    @lru_cache(None)
    def dp(start, end):
        if start > end:
            return 0
        if start == end:
            return 1
        return min(dp(start+1, end) + 1, dp(start, end-1) + 1)
    return dp(0, len(arr)-1)

