
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
    left, right = 0, len(arr) // 2
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] != arr[left] and arr[mid] != arr[right]:
            return mid
        left = mid + 1
        right = mid - 1
    return left
