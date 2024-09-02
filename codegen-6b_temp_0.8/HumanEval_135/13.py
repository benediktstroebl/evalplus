
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr:
        return -1

    arr.sort(reverse=True)
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if mid < end and arr[mid] <= arr[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1

    return start

