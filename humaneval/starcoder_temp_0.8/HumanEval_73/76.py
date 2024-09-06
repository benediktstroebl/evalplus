
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
    # # Approach 1: Brute force. Time complexity = O(n^2)
    # smallest_count = len(arr)
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if arr[i]!= arr[j]:
    #             arr[i], arr[j] = arr[j], arr[i]
    #             if is_palindrome(arr):
    #                 smallest_count = min(smallest_count, abs(i - j))
    #             arr[i], arr[j] = arr[j], arr[i]
    # return smallest_count

    # Approach 2: Dynamic programming. Time complexity = O(n)
    dp = [0] * len(arr)
    dp[0] = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + 1
    return min(dp)

