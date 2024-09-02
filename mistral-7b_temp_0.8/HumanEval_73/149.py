
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
    ## Write your code here.
    # Note: you are not allowed to return the smallest change, but to make the array palindromic

    palindrome_index = len(arr) // 2
    palindrome_arr = list(arr[0:palindrome_index])
    palindrome_arr = palindrome_arr[::-1]

    counter = 0
    for i in range(palindrome_index):
        if arr[i] != palindrome_arr[i]:
            counter += 1

    return counter
