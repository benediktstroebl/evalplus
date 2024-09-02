
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
    # a palindrome is a string that reads the same forward as backward
    # "racecar" is a palindrome

    # first reverse the array
    arr.reverse()

    # then compare the elements to the new array, and return the number of elements that are different
    diff_counter = 0
    for i in range(len(arr)):
        if arr[i] != arr[i+1]:
            diff_counter += 1
    return diff_counter

