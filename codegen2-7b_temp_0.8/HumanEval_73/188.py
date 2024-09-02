
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
    arr_length = len(arr)

    if arr_length == 1:
        return 0

    current_max = max(arr)
    current_min = min(arr)

    while current_min < current_max:
        next_max = current_max
        current_max = current_max + current_min

        next_min = current_min
        current_min = current_min + current_max

        if current_min < next_max:
            current_min = next_min

    return next_max - current_max +
