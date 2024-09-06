
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
    n = len(arr)
    if n <= 1:
        return 0
    left = 0
    right = n-1
    num = arr[left]
    while left < right:
        if num == arr[right]:
            break
        left += 1
        right -= 1
    if left >= right:
        return n // 2
    start = left
    end = right
    left = start + 1
    right = end - 1
    while left <= right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] == arr[end]:
            left += 1
        elif arr[right] == arr[start]:
            right -= 1
        else:
            return n - 1
    return n - (end - left + 1 + start - right)
