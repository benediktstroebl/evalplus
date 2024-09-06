def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes
    """
    # your code here
    n = len(arr)
    # calculate the middle index
    mid = n // 2
    # initialize the count of changes to 0
    change_count = 0
    # iterate through array elements starting from the middle
    for i in range(mid, -1, -1):
        # check if the current element is different from the counterpart on the opposite side of the array
        if arr[i] != arr[n-1-i]:
            # increment the change count
            change_count += 1
        # in the case of a bilateral mirror, check both sides
        elif i != mid and arr[i] != arr[mid]:
            # increment the change count
            change_count += 1
    # return the change count
    return change_count