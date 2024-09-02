
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
    # initialize the count to the length of the array
    count = len(arr)
    # iterate through the array
    for i in range(len(arr)):
        # if the current index is not equal to the last index
        if i != len(arr) - 1:
            # and the current index is not equal to the last index - 1
            if arr[i] != arr[len(arr) - 1 - i]:
                # decrement the count by 1
                count -= 1
    return count

