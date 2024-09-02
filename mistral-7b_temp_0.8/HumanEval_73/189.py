
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

    longest_palindromic_length = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i):
            if arr[j] == arr[j+i] and i + 1 > longest_palindromic_length:
                longest_palindromic_length = i + 1
    return len(arr) - longest_palindromic_length

