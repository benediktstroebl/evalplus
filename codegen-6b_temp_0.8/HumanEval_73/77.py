
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
    min_c = float('inf')

    # first find the number of elements in the array to make it palindromic
    for i in xrange(n):
        count = 0
        for j in xrange(n//2):
            if arr[i] != arr[n-1-j]:
                count += 1

        if count <= min_c:
            min_c = count

    return min_c

