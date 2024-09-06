
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
    first = arr[0]
    second = arr[1]
    if first == second:
        return 0
    if len(arr) <= 2:
        return len(arr) - 1
    first_index = len(arr) - 1
    second_index = len(arr) - 2
    while second_index > 0 and arr[first_index] > arr[second_index]:
        second_index -= 1
    first_index += 1
    return second_index
