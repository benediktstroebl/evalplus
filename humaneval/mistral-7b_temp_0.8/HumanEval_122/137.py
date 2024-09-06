
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
    if not arr:
        return 0
    if k > len(arr):
        return 0
    # 00 -> 99
    if k <= 99:
        res = 0
        for i in range(k):
            res += arr[i]
        return res
    elif k <= 999:
        return sum([arr[i] for i in range(k) if 100 <= arr[i] < 1000])
    elif k <= 9999:
        return sum([arr[i] for i in range(k) if 1000 <= arr[i] < 10000])
    elif k <= 99999:
        return sum([arr[i] for i in range(k) if 10000 <= arr[i] < 100000])
    elif k <= 999999:
        return sum([arr[i] for i in range(k) if 100000 <= arr[i] < 1000
