
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
    # 0 <= sum(arr[i]) <= 999
    # 0 <= sum(arr[i]) - arr[i] <= 999
    # 0 <= sum(arr[i]) - 999 <= 999
    # 0 <= sum(arr[i]) - 1000 <= 999
    # 0 <= k - (sum(arr[i]) - 1000) <= k
    # 0 <= k - (sum(arr[i]) - 1000) <= 999
    # 0 <= k - (sum(arr[i]) - 1000) <= k - 1
    # 0 <= sum(arr[i]) - 1000 <= k - 1

    result = 0
    for i, v in enumerate(arr):
        if i >= k:
            break
        v = v - (1000 if v >= 1000 else 0)
        result += v
    return result

