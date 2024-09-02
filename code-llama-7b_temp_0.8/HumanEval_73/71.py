
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

    # find the middle
    length = len(arr)
    middle = length // 2

    # populate the left side
    left = []
    left.append(arr[0])
    for i in range(1, middle + 1):
        left.append(arr[i])

    # populate the right side
    right = []
    if length % 2 == 0:
        for i in range(length - 1, middle, -1):
            right.append(arr[i])
    else:
        for i in range(length - 1, middle + 1, -1):
            right.append(arr[i])

    # find the number of changes to make the array palindromic
    count = 0
    i = 0
    for l, r in zip(left, right):
        if l != r:
            count += 1
        i += 1

    return count
