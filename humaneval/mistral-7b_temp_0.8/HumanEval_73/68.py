
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

    arr = list(set(arr))
    arr.sort()
    n = len(arr)
    def bfs(arr, i):
        if i == n:
            return [i]
        if arr[i] == arr[n-i-1]:
            return bfs(arr, i+1)
        else:
            x = bfs(arr, i+1)
            y = bfs(arr, i+2)
            if len(x) < len(y):
                return x
            else:
                return y
    return n - len(bfs(arr, 0))
