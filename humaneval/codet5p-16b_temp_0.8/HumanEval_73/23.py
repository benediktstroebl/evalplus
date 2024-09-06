
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

    if arr is None or len(arr) == 0:
        return -1

    if len(arr) == 1:
        return 0

    # initialize the counts
    counts = {
        0: [],
        1: [],
        2: [],
        3: []
    }

    # loop through the array
    for i in arr:
        count = 0
        if i % 2 == 1:
            count += 1
        if i % 3 == 0:
            count += 1
        if i % 5 == 0:
            count += 1
        counts[count].append(i)

    # print(counts)

    count = 0
    if len(counts[0]) > 0:
        count += 1
    if len(counts[1]) > 1:
        count += 1
    if len(counts[2]) > 1:
        count += 1
    if len(counts[3]) > 1:
        count += 1

    return count


