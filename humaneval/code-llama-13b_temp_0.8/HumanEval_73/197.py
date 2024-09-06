
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
    left_ptr = 0
    right_ptr = len(arr) - 1
    change_count = 0
    while left_ptr <= right_ptr:
        if arr[left_ptr] != arr[right_ptr]:
            change_count += 1
        left_ptr += 1
        right_ptr -= 1
    return change_count

