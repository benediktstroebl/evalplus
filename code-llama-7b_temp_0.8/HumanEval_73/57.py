
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
    # Reverse Array
    reversed_arr = arr[::-1]
    reversed_arr_string = str(reversed_arr)

    # Convert array to string
    arr_string = str(arr)

    # Get the differences between the string and reversed string
    diff = len(arr_string) - len(arr_string.replace(reversed_arr_string, ""))

    # Return the diff
    return diff

