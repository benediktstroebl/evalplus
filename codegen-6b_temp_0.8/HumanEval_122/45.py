
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
    arr = list(arr)
    res = 0
    i = 0
    while i < k:
        res += (k - i) * arr[i]
        i += 1
    j = 0
    while i < len(arr):
        if j < len(arr) - i:
            res += ((len(arr) - i - 1) + j) * arr[i + j]
        elif j == len(arr) - i:
            res += j * arr[i + j]
        j += 1
        i += 1
    return res

