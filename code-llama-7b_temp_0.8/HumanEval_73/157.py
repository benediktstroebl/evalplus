
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
    # if there is a palindrome, return 0
    if check_if_palindrome(arr):
        return 0
    #if it's not a palindrome, check if it's a flipped palindrome
    elif check_if_flip(arr):
        return len(arr)/2
    else:
        #if it's not a flip, it's a hard one
        return find_palindrome(arr)

