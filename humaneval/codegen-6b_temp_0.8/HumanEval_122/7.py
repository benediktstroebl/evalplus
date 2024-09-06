
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
    s = 0
    for i in range(min(k, n)):
        s += arr[i]
    if k >= n:
        return s

    if k == 1:
        a = min(arr[:n - k + 1])
        b = max(arr[:n - k + 1])
        return s + sum([int(str(a)[-1]) + int(str(b)[0])] + [int(str(b)[-1])] * 2)

    if k == 2:
        a = min(arr[:n - k + 1])
        b = max(arr[:n - k + 1])
        return s + sum([int(str(a)[-1]) + int(str(b)[0])] + [int(str(b)[-1])] * 2) + sum(
            [int(str(a)[0])] + [int(str(b)[0])] * 2)

    if k == 3:
        a = min(arr[:n - k + 1])
        b = max(arr[:n - k + 1])
        c = max(arr[:n - k + 2])
        return s + sum([int(str(a)[-1]) + int(str(b)[0])] + [int(str(b)[-1])] * 2) + sum(
            [int(str(a)[0])] + [int(str(b)[0])] * 2) + sum([int(str(c)[0])] + [int(str(c)[-1])] * 2)

