
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
    # 1st solution
    # O(n) time | O(n) space
    # n = len(arr)
    # res = 0
    # for i in range(k):
    #     res += arr[i]
    # return res

    # 2nd solution
    # O(n) time | O(1) space
    n = len(arr)
    res = 0
    i = 0
    while i < k:
        res += arr[i]
        i += 1
    prev = res % 100
    if prev > 9:
        prev -= 10
    res = prev
    for i in range(k, n):
        res += (arr[i] % 100)
        if res % 100 > 9:
            res %= 100
    return res % 100
