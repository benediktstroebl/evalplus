
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
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1
    f = [None for _ in range(len(arr))]
    f[0] = 0
    f[1] = 1
    for i in range(2, len(arr)):
        f[i] = 2 * (f[i - 1] + 1)
        if arr[i - 1] == arr[i]:
            f[i] = min(f[i], f[i - 2] + 1)
    if f[len(arr) - 1] == 2 * (f[len(arr) - 2] + 1):
        return f[len(arr) - 1]
    else:
        return f[len(arr) - 1]

