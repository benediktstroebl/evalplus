
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
    palindrome_found = False
    n = len(arr)

    if n == 0 or n == 1:
        return 0

    i = 0
    while not palindrome_found:
        if arr[i] == arr[n - i - 1]:
            i += 1
            if i == n // 2:
                palindrome_found = True
        else:
            if arr[i] < arr[n - i - 1]:
                n = n - i - 1
            else:
                n = n - i
                i = 0

    return n
