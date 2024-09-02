
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    dp = {}
    for i in range(len(arr)-1):
        j = i+1
        if arr[i] <= arr[j]:
            dp[i] = -1
        else:
            dp[i] = max(dp.get(i, -1), j-1)
    return dp.get(len(arr)-1, -1)