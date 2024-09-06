
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def find_min_non_ge(arr):
        min_idx = -1
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1] and min_idx == -1:
                min_idx = i
            elif arr[i] < arr[i-1] and min_idx != -1:
                return -1
        return min_idx

    def func(arr):
        min_idx = find_min_non_ge(arr)
        if min_idx == -1:
            return -1
        else:
            return arr.index(arr[min_idx])

    return func

