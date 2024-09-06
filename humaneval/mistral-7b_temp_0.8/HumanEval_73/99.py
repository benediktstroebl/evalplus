
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
    # Write your code here.
    # need to figure out the correct steps to take to make the array palindromic
    # check that the array is palindromic and if not, how many steps need to be taken to make it so
    # check the value at the middle of the array (index 3) and compare to the value at the end of the array (index 7)
    # if the values are not equal, then the array is not palindromic
    # check the values at index 3 and index 6 and if they are equal, then the array is palindromic
    # if the array is not palindromic, then find the smallest change that needs to be made to the array
    # count the number of changes that need to be made to the array to make it palindromic

    # iterate over the array and count the number of changes that need to be made to the array to make it palindromic

    # create an array called arr_copy that is a copy of the arr array
    arr_copy = arr.copy()

    # iterate over the array and check if the array
