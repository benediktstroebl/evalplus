
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

    # Counters
    forward = {}
    backward = {}

    # Loop through array to populate counters
    for i in range(len(arr)):
        forward[arr[i]] = forward.get(arr[i], 0) + 1
        backward[arr[len(arr)-i-1]] = backward.get(arr[len(arr)-i-1], 0) + 1

    count = 0

    # Loop through counters
    for k, v in forward.items():
        if v < backward[k]:
            count += backward[k] - v

    return count


