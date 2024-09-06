
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
    if len(arr) <= 1:
        return 0

    forward_index = 0
    backward_index = len(arr) - 1

    count = 0
    while forward_index < backward_index:
        if arr[forward_index] == arr[backward_index]:
            forward_index += 1
            backward_index -= 1
        elif arr[forward_index] == arr[backward_index] + 1 or arr[forward_index] == arr[backward_index] - 1:
            forward_index += 1
            backward_index -= 1
            count += 1
        else:
            forward_index += 1
            backward_index -= 1
            count += 2

    return count
