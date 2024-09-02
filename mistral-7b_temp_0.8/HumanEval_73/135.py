
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

    # Solution:
    # Convert the array to a list
    arr = list(arr)

    # Sort the array in place
    arr.sort()

    # Calculate the difference between the first and last element of the array
    diff = arr[0] - arr[-1]

    # If the array is already palindromic, return 0
    if diff == 0:
        return 0

    # If the array is not palindromic, return the difference between the first and last element of the array
    return diff

    # your code here
