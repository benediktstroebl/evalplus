
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
    def is_palindrome(arr):
        left = 0
        right = len(arr) - 1
        while left <= right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True

    if is_palindrome(arr):
        return 0
    palindrome = 0
    right = len(arr) - 1
    while right > 0:
        if is_palindrome(arr):
            palindrome = len(arr) - right - 1
            break
        right -= 1
        arr[right], arr[right + 1] = arr[right + 1], arr[right]

    return palindrome

