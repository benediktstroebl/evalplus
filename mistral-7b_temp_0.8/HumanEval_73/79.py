
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
    # TODO: Write your code here
    count = 0
    arr = [0, 1, 2]
    arr = [3, 4, 5, 6, 7, 8]
    arr = [4, 5, 6, 7]
    arr = [4, 5, 6, 7, 8]
    arr = [4, 5, 6, 7, 8, 9]
    arr = [4, 5, 6, 7, 8, 9, 10]
    arr = [4, 5, 6, 7, 8, 9, 10, 11]
    arr = [4, 5, 6, 7, 8, 9, 10, 11, 12]
    arr = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    arr = [4, 5, 6, 7, 8, 9,
