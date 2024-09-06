
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
    result = 0
    left_pointer = 0
    right_pointer = len(arr) - 1
    while left_pointer < right_pointer:
        if arr[left_pointer] == arr[right_pointer]:
            left_pointer += 1
            right_pointer -= 1
        else:
            left_pointer += 1
            result += 1
    return result
