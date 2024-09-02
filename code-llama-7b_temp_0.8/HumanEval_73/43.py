
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
    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    newarr = []
    for i in arr:
        newarr.append(i)
    newarr.sort()
    arr = arr[::-1]
    # print(arr)
    # print(newarr)
    i = 0
    j = 0
    count = 0
    while i < len(arr):
        if arr[i] == newarr[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
            count += 1
            i += 1
        if j == len(newarr):
            j = 0
    return count

