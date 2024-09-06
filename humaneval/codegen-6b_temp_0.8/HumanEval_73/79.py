
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
    # base case - if the array is already palindromic, return 0
    if is_palindromic(arr):
        return 0

    # otherwise, get the absolute difference between left most and right most elements
    diff = abs(arr[0] - arr[-1])

    # loop through the array, starting with first element and moving backwards,
    # updating the difference as you move forward
    i = 0
    while i < len(arr) - 1:
        diff = min(diff, abs(arr[i] - arr[i+1]))
        i += 1

    # finally, return the updated difference
    return diff

