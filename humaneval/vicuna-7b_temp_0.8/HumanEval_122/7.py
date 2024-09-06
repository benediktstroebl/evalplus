
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
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    k = max(k, 1)
    i = 0
    while i < k:
        a = arr[i]
        if a < 10:
            j = 0
            while j < n and (arr[j] < 10 or arr[j] > 9 + (a/10)):
                j += 1
            if j == n:
                return 0
        i += 1
    return 0
