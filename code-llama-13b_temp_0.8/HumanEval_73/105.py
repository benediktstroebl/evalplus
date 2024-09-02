
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
    if len(arr) == 0:
        return 0
    left_index = 0
    right_index = len(arr) - 1
    changes = 0
    while left_index < right_index:
        if arr[left_index] != arr[right_index]:
            changes += 1
            # If the left value is greater than the right value, decrease the left value.
            if arr[left_index] > arr[right_index]:
                arr[left_index] -= 1
            # Otherwise, increase the right value.
            else:
                arr[right_index] += 1
        left_index += 1
        right_index -= 1
    return changes
