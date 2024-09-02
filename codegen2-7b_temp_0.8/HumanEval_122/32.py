
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
    res = 0
    for i in range(k):
        t = int(str(arr[i])[0])
        if t >= 10:
            res += t
        elif t >= 2:
            res += 1
    for i in range(k, len(arr)):
        t = int(str(arr[i])[0])
        if t >= 10:
            res += t
            res += 10
        else:
            res += t
    return
