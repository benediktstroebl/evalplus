
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

    s = sum(arr)
    half = s // 2
    dp = [float("inf")] * (half + 1)
    for i in range(half + 1):
        if arr[i] == half:
            dp[i] = 1
        if arr[i] > half:
            continue
        if arr[i] < half and i == arr[i]:
            dp[i] = 1
        for j in range(i + 1, half + 1):
            if arr[i] + arr[j] > half:
                break
            if arr[i] + arr[j] < half:
                continue
            if dp[i] + 1 < dp[j]:
                dp[j] = dp[i] + 1
    return dp[-1]
