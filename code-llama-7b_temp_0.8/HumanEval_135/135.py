
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    l = len(arr)
    if l == 0 or l == 1:
        return -1
    elif l == 2:
        return -1 if arr[0] >= arr[1] else 1

    mid = l // 2
    left = arr[:mid]
    right = arr[mid:]
    # print(left, right)

    left_max = max(left)
    right_max = max(right)

    if left_max >= right_max:
        return can_arrange(left)
    else:
        return mid + can_arrange(right)

