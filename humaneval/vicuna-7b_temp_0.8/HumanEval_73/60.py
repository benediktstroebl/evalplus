
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
    min_change = n
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for i, j, k in [(i, j, k) for i in range(n) for j in range(i) for k in range(j) if (i, j, k) != (0, 0, 0)]:
                    if (arr[i] != arr[k] and arr[j] != arr[i] and arr[j] != arr[k]):
                        return min_change
                        break
                else:
                    return min_change
    return min_change
