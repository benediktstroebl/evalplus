
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
    # k = 0
    # m = 0
    # n = len(arr)
    # for i in range(n):
    #     k += arr[i]
    #     m += arr[n - 1 - i]
    # if k != m:
    #     return -1
    # t = [0] * 10001
    # ans = 0
    # for i in range(n):
    #     t[arr[i]] += 1
    # for i in range(1, 10001):
    #     t[i] += t[i - 1]
    #     if t[i] - t[i - 1] % 2:
    #         ans += t[i] - t[i - 1]
    # return ans / 2
    return 0

