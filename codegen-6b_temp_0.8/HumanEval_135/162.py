
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) == 0:
        raise ValueError("Can't arrange an empty array.")

    arr_dict = {}
    for i in range(len(arr)):
        arr_dict[arr[i]] = i

    for i in range(len(arr)):
        if arr[i] < arr[i - 1]:
            return -1

    for i in range(len(arr)):
        if arr[i] != i:
            t = arr[i]
            j = i - 1
            while arr[j] > t and j >= 0:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = t
            arr_dict[t] = j + 1

    return arr_dict

