
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
    import math
    arr_set = set(arr)
    palindromics = []
    for x in arr_set:
        count = 0
        for y in arr:
            if y!= x and y > x and arr.count(x-y):
                count += 1
        if arr.count(x) > arr.count(x+1):
            count += arr.count(x) - arr.count(x+1)
        palindromics.append(count)
    return min(palindromics)
