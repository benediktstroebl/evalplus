
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
    """
    Method 1:
    """
    n = len(arr)
    ans = 0
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            ans += 1
    if n % 2 == 1:
        i = n // 2
        if arr[i] != arr[n - i]:
            ans += 1
    return ans

    """
    Method 2:
    """
    n = len(arr)
    ans = 0
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            if arr[i] == arr[i + 1] and arr[n - 1 - i] == arr[n - 2 - i]:
                ans += 1
            else:
                return -1
    if n % 2 == 1:
        i = n // 2
        if arr[i] != arr[n - i]:
            ans += 1
    return ans
