
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
    if n == 0:
        return 0
    if n == 1:
        return 0
    l = arr[:n//2]
    r = arr[n//2:]
    l.reverse()
    count = 0
    for i in range(len(l)):
        if l[i]!= r[i]:
            count += 1

    return count + smallest_change(l) + smallest_change(r)

