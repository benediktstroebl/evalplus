
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
    n = len(arr)
    # initialize a variable to store the min number of changes
    changes = float('inf')
    # initialize a variable to store the index of the next change
    next_change_index = 0
    # loop through the array
    for i in range(n):
        # check if the element is the next element to change
        if arr[i] != arr[next_change_index]:
            # increment the number of changes
            changes -= 1
            # update the index of the next change
            next_change_index = (next_change_index + 1) % n
        else:
            next_change_index = (next_change_index + 1) % n
    return changes
