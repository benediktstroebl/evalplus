
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
    if len(arr) == 1:
        return 0
    is_palindrome = {}
    for i in range(len(arr)):
        is_palindrome[i] = {}
        for j in range(i, len(arr)):
            is_palindrome[i][j] = is_palindrome[i][j - 1] or is_palindrome[i + 1][j] if i + 1 < j else arr[i] == arr[j]
    return min(is_palindrome[0][-1], is_palindrome[0][-2]) if len(arr) > 2 else is_palindrome[0][-1]
