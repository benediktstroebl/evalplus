
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
    min_change = float('inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(j, len(arr)):
                for l in range(k, len(arr)):
                    for n in range(i, j-1, -1):
                        for m in range(j-1, k-1, -1):
                            for o in range(k-1, l-1, -1):
                                for p in range(l-1, n-1, -1):
                                    arr[i], arr[j] = arr[j], arr[i]
                                    arr[k], arr[l] = arr[l], arr[k]
                                    arr[n], arr[o] = arr[o], arr[n]
                                    arr[p], arr[m] = arr[m], arr[p]
    return min_change