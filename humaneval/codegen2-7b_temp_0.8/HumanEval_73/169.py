
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
    if len(arr) == 1:
        return 1

    _arr = arr.copy()

    n = len(_arr)

    for i in range(n):
        for j in range(i+1, n):
            if _arr[i] == _arr[j]:
                _arr[j] -= 1
                if _arr[j] == -1:
                    _arr[i] -= 1
                    if _arr[i] == 0:
                        _arr[j] -= 1
                    break

    return min(len(_arr), n
