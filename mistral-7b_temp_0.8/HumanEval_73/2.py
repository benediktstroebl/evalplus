
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
    arr = sorted(arr)
    left_index = 0
    right_index = len(arr) - 1
    smallest = float('inf')
    # if first and last element are same, it is already palindromic
    if arr[left_index] == arr[right_index]:
        return 0
    # if first element is not equal to last element
    while left_index < right_index:
        if arr[left_index] != arr[right_index]:
            smallest = min(smallest, right_index - left_index + 1)
            left_index += 1
        else:
            right_index -= 1
    return smallest
