
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

    start, end = 0, len(arr)-1
    mid = (start + end) / 2

    while start < end:
        print "Start: %s, End: %s, Mid: %s" % (start, end, mid)
        print "Start[mid]: %s, End[mid]: %s" % (arr[start] % arr[mid], arr[end] % arr[mid])

        if arr[start] % arr[mid] == 0:
            start += 1
        elif arr[end] % arr[mid] == 0:
            end -= 1
        else:
            return arr[mid] + 1

