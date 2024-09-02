
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

    # get middle index
    mid = (n - 1) // 2

    # get two halves
    left = arr[0:mid + 1]
    right = arr[mid::-1]

    # check if two halves are same
    if left == right:
        return 0

    # find out the differences between left and right
    diffs = [0] * n
    i = 0
    while i < len(left) and i < len(right):
        if left[i]!= right[i]:
            diffs[i] = abs(left[i] - right[i])
        i += 1

    # find the minimum
    i = 0
    while i < len(diffs) and diffs[i] == 0:
        i += 1
    return i
