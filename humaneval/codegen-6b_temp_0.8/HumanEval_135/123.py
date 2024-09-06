
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def helper(arr, mid):
        for i in range(mid, len(arr)):
            if arr[i] <= arr[mid]:
                return i
        return -1
    ans = -1
    for i in range(len(arr)):
        mid = i
        if can_arrange(arr[0:mid]) > -1:
            ans = max(ans, can_arrange(arr[0:mid]))
        if can_arrange(arr[mid:len(arr)]) > -1:
            ans = max(ans, can_arrange(arr[mid:len(arr)]))
    return ans
