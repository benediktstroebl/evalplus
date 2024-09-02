
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
    n = len(arr)
    if n == 0 or k == 0:
        return 0
    if k > n:
        k = n
    ans = 0
    for i in range(k):
        ans += arr[i]
    prev_two = 0
    idx = k
    while idx < n:
        ans += arr[idx] - prev_two
        prev_two = arr[idx]
        idx += 1
    return ans
