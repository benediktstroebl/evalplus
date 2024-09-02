
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
    start_pos = 0
    end_pos = len(arr) - 1

    # First, find the middle of the array.
    middle_pos = (start_pos + end_pos) / 2

    # Check if the array is palindromic.
    while start_pos < middle_pos:
        if arr[start_pos] == arr[end_pos]:
            start_pos += 1
            end_pos -= 1
        else:
            return (end_pos - start_pos) + 1

    return 0

