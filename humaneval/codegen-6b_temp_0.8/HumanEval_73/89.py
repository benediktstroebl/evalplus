
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
    # base case: if array is empty, we need 0 to return.
    if not arr:
        return 0

    # this is a greedy algorithm.
    # we want to change the smallest number of elements.
    # we are looking for the smallest subarray with the lowest number of elements.
    # we can do this by iterating over the array, comparing arrays of increasing size.
    # we loop until we reach a subarray that is already palindromic.
    # we need to return the length of the subarray.

    # store a running sum of changes
    running_sum = 0
    # store the sum of array so far.
    best_sum = arr[0]
    # store the minimum number of changes we need
    best_min_changes = None
    for i in range(len(arr)):
        # the running sum of array is the sum of the array so far plus the element at the current index
        running_sum += arr[i]
        # we have a best_sum so far.
        if running_sum < best_sum:
            # the best_sum we have so far is the best_sum found so far
            best_sum = running_sum
            # the best_min_changes we have so far is the minimum number of changes we need to make to the array so far
            best_min_changes = i
        # when we reach a subarray that turns out to be palindromic, we can stop
        if running_sum == 0:
            break

    return best_min_changes

