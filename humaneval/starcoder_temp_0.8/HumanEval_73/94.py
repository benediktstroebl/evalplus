
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
    # find min and max values in array
    min_val, max_val = min(arr), max(arr)

    # convert all elements to negative values
    arr = [-val for val in arr]
    # add difference between max and min
    arr = [val + abs(max_val) - abs(min_val) for val in arr]

    # count the number of negative values
    return arr.count(-1)
