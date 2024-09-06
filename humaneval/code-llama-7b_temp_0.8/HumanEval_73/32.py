
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
    if n < 2:
        return 0

    # Convert to sum of differences of adjacent values
    diffs = [0] * n
    diffs[0] = arr[0]
    for i in range(1, n):
        diffs[i] = diffs[i-1] + arr[i]

    # Start at the end and work backwards
    diffs_rev = [0] * n
    diffs_rev[n-1] = arr[n-1]
    for i in reversed(range(n-1)):
        diffs_rev[i] = diffs_rev[i+1] + arr[i]

    # The diffs are the same, return 0
    if diffs == diffs_rev:
        return 0

    # The diffs are not the same, find the best number of changes
    res = float('inf')
    for i in range(n-1):
        res = min(res, abs(diffs[i] - diffs_rev[i+1]))

    return res

