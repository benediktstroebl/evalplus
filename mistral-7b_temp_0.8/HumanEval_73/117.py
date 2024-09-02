
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
    l = len(arr)
    if l < 3:
        return 0
    if l % 2 == 0:
        mid_index = l // 2 - 1
    else:
        mid_index = l // 2
    left, right = 0, l - 1
    while left <= mid_index and right > mid_index:
        if arr[left] != arr[right]:
            return 1
        else:
            left += 1
            right -= 1
    return 0

