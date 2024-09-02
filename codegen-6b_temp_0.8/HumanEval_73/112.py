
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
    prev_prev = arr[:]
    prev = arr[:]
    changes = 0
    while prev != prev_prev:
        changes += 1
        #print(changes, prev, prev_prev)
        prev_prev[:] = prev[:]
        prev[:] = [a for a in arr if max(a-1, 0) == min(a+1, len(arr)-1)]
    return changes

