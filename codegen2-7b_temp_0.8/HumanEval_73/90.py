
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
    def is_palindromic(arr):
        return arr == arr[::-1]
    if is_palindromic(arr):
        return 0
    arr = sorted(arr)
    left = right = 0
    while right < len(arr):
        if arr[right] - arr[left] < 3:
            right += 1
            left = right
        else:
            if is_palindromic(arr[left:right]):
                return min(right - left, right - left + 1)
            right += 1
    return -1
