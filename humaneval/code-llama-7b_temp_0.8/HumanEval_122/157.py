
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
    MOD = 1000000007
    # compute prefix sums
    prefix_sums = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix_sums[i+1] = prefix_sums[i] + arr[i]
    # compute the sum of the first k elements
    result = prefix_sums[k]
    # compute sum of the first k digits
    k = min(k, len(arr))
    for i in range(k):
        if len(str(arr[i])) <= 2:
            result -= arr[i]
    return result % MOD


