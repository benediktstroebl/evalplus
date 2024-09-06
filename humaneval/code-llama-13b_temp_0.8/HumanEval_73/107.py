
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
    if len(arr) <= 1:
        return 0
    if len(arr) == 2:
        return 1
    palindrome = [False] * len(arr)
    if arr[0] == arr[-1]:
        palindrome[0] = True
        palindrome[-1] = True
    for i in range(1, len(arr) - 1):
        if arr[i] == arr[i - 1]:
            palindrome[i] = True
        if arr[i] == arr[i + 1]:
            palindrome[i] = True
    changes = 0
    for i in range(len(palindrome)):
        if not palindrome[i]:
            changes += 1
            for j in range(1, min(i + 1, len(arr) - 1 - i)):
                if i - j >= 0 and i + j < len(arr) and arr[i - j] == arr[i + j]:
                    palindrome[i - j] = True
                    palindrome[i + j] = True
                elif i + j >= len(arr) and i - j < 0 and arr[i - j] == arr[i + j]:
                    palindrome[i - j] = True
                    palindrome[i + j] = True
                elif i - j >= 0 and arr[i - j] == arr[i + j]:
                    palindrome[i - j] = True
                elif i + j < len(arr) and arr[i - j] == arr[i + j]:
                    palindrome[i + j] = True
    return changes

