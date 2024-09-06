
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
    # first we need to find the median
    if len(arr) % 2 == 0:
        # if the length is even we need to find the average of the two middle elements
        median = (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        # if the length is odd we find the middle element
        median = arr[len(arr) // 2]
    # then we compare all elements to the median, if they are greater than the median we add 1 to the number of
    # changes, if they are lower than the median we add 1 to the number of changes
    changes = 0
    for i in arr:
        if i > median:
            changes += 1
        elif i < median:
            changes += 1
    return changes

