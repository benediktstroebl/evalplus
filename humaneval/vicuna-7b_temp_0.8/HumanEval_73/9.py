
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
    arr = sorted(arr)
    n = len(arr)
    count = [0] * n
    for i in range(n):
        count[arr[i]] += 1
    max_count = max(count)
    for i in range(n):
        count[arr[i]] -= max_count
        if count[arr[i]] < 0:
            break
    return n - i
