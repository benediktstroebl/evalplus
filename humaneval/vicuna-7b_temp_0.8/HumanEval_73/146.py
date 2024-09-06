
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
    min_diff = n * n
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                for l in range(k + 1, n):
                    if arr[i] != arr[j] and arr[j] != arr[k] and arr[k] != arr[l] and arr[l] != arr[i]:
                        min_diff = min(min_diff, abs(arr[i] - arr[j])) + abs(arr[j] - arr[k]) + abs(arr[k] - arr[l]) + abs(arr[l] - arr[i])
    return min_diff