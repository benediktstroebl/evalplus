
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
    bitmask = 0
    for i in range(k):
        bitmask |= (1 << arr[i])

    def sum_to_k(s):
        r = 0
        for i in range(k):
            if s & (1 << arr[i]) == 0:
                r += arr[i]
        return r

    r = sum_to_k(bitmask)
    for i in range(k, len(arr)):
        bitmask |= (1 << arr[i])
        r += sum_to_k(bitmask) - sum_to_k(bitmask - 1)
    return r

