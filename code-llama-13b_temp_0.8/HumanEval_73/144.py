
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
    if len(arr) < 2:
        return 0
    left, right = 0, len(arr) - 1
    left_to_right = {}
    right_to_left = {}
    # check how many left to right values are different
    while left <= right:
        if arr[left] != arr[right]:
            left_to_right[arr[left]] = arr[right]
        left += 1
        right -= 1

    if len(left_to_right) == 0:
        return 0

    right = 0
    # check how many right to left values are different
    while right < len(arr):
        if arr[right] != arr[left_to_right[arr[right]]]:
            right_to_left[arr[right]] = arr[left_to_right[arr[right]]]
        right += 1

    return len(left_to_right) + len(right_to_left)

