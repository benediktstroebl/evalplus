
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

    result = 0
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 0
        d[i] += 1
    if len(d) == 1:
        return 0
    for i in d:
        if d[i] % 2 == 1:
            result += 1
        if d[i] % 2 == 1:
            d[i] = d[i] // 2
    return result
