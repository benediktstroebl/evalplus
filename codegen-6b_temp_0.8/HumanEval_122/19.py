
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
    lo, hi = 0, k - 1
    while lo < hi:
        if arr[lo] + arr[hi] >= 10:
            num = arr[lo] + arr[hi]
            idx = num // 10
            val = num - idx * 10
            arr[lo] = val
            arr[hi] = idx
            lo += 1
            hi -= 1
        else:
            hi -= 1
    return sum(arr[:k])

