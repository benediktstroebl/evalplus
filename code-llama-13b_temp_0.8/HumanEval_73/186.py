
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

    first_index = 0
    last_index = len(arr) - 1
    changes = 0
    while first_index <= last_index:
        if arr[first_index] != arr[last_index]:
            changes += 1
            if arr[first_index] < arr[last_index]:
                arr[first_index] += 1
            else:
                arr[last_index] -= 1
        first_index += 1
        last_index -= 1
    return changes

