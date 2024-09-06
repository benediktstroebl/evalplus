
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
    if arr == arr[::-1]:
        return 0

    if len(arr) == 1:
        return 1

    def check_palindrome(s, e):
        for i in range(s, e):
            if arr[i] != arr[e - i - 1]:
                return False

        return True

    min_change = len(arr)
    for i, num in enumerate(arr):
        if i + 1 < len(arr):
            if check_palindrome(i + 1, i + 1 + min_change):
                return min_change
        if i > 0:
            if check_palindrome(i - 1, i + min_change):
                return min_change
        min_change = min(min_change, len(arr) - i - 1)

    return len(arr) - min_change

