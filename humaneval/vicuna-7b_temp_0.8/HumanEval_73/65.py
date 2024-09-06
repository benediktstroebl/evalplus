
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
    # check if array is already palindromic
    if arr == sorted(arr):
        return 0

    # initialize the count of change to the number of elements in the array
    count = len(arr)

    # start checking from the second element
    i = 1

    while i < len(arr):
        # find the minimum difference between the current element and the previous element
        min_diff = 1000000000
        for j in range(i - 1, len(arr)):
            diff = (arr[j] - arr[i - 1]) * (arr[j] - arr[i - 1])
            if diff < min_diff:
                min_diff = diff
        if min_diff == 0:
            # if the difference is 0, means the element is already the middle of the array
            count -= 1
        else:
            # otherwise, the difference is 1 or more, so we can change the current element to a different element
            count -= min_diff
            i += 1

    return count