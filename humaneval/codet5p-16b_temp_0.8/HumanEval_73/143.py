
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

    import numpy as np
    arr = np.array(arr)
    length = len(arr)
    l = []
    for i in range(length):
        a = np.array(arr)
        a[i] = np.array(arr)[length - i - 1]
        l.append(a)
    print(l)
    max_change = 0
    for item in l:
        a = np.where(item!= arr)
        if len(a[0]) > max_change:
            max_change = len(a[0])
    return max_change




