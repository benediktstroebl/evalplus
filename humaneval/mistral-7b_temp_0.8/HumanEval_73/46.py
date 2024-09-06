
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
    # Initially, we are going to consider all elements are changed into 0
    diff = 0
    # Go through the array, counting the changes required to make each element palindromic
    for i in range(len(arr)):
        if arr[i] > i:
            # If the current element is not a palindrome, we need to change it to a palindrome
            diff += abs(arr[i] - i)
    return diff

