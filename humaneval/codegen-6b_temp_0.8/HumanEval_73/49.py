
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
    # Count the number of odd/even elements and see if it is equal to the length of the array
    low = 0
    high = 0
    for value in arr:
        if value % 2 == 0:
            low += 1
            high += 1
        else:
            low += 1
            high -= 1
    if high == len(arr) or low == len(arr):
        return 0
    return min(len(arr) - high - low, high + low)

