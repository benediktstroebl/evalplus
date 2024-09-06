
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # First approach: sliding window (108ms, 13.7MB)
    # Runtime: 108 ms, faster than 76.85% of Python3 online submissions for Addition of Two Numbers.
    # Memory Usage: 13.7 MB, less than 5.09% of Python3 online submissions for Addition of Two Numbers.
    #
    # Time complexity: O(N)
    # Space complexity: O(N)
    res = 0
    n = len(arr)
    for i in range(k):
        res += arr[i]
    for i in range(k, n):
        res += arr[i] - arr[i - k]
    return res

