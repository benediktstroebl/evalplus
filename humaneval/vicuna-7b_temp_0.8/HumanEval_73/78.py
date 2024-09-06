
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
        mid = (left + right) // 2
        if arr[left] != arr[mid]:
            if mid != left:
                arr[left], arr[mid] = arr[mid], arr[left]
            if mid < right:
                arr[mid], arr[right] = arr[right], arr[mid]
            left += 1
            right -= 1
    return left