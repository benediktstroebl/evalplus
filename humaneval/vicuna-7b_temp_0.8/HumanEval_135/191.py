
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def get_index(arr, val):
        if val > arr[0]:
            return -1
        for i in range(1, len(arr)):
            if val >= arr[i]:
                return i
        return 0

    arr = sorted(arr)
    index = get_index(arr, arr[0])
    if index == -1:
        return -1
    else:
        return index + 1

test = [1, 2, 3, 2, 4, 3, 5, 4, 5, 5, 5]
result = can_arrange(test)
