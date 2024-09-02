
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
    if len(arr) < 2:
        return 0
    if len(arr) == 2:
        return min(arr[1] - arr[0], arr[0] - arr[1])
    min_change = sys.maxsize
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == arr[j + 1]:
                min_change = min(min_change, j - i)
    return min_change
