
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr: return -1
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left+right)//2
        if arr[mid] >= arr[mid-1]:
            left = mid+1
        elif arr[mid] < arr[mid-1]:
            right = mid-1
        else: return mid
    return right if arr[right] <= arr[left-1] else -1
