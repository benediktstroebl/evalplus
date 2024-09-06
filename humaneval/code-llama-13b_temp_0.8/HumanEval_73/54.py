
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

    n = len(arr)
    if n == 1:
        return 0

    ans = n
    d = {arr[0]: 0}

    for i in range(1, n):
        if arr[i] not in d:
            d[arr[i]] = i
        else:
            index = d[arr[i]]
            if index >= i:
                ans = min(ans, i - index)
            else:
                ans = min(ans, index - i)

    return ans

