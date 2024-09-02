
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
    if len(arr) <= k:
        return sum(arr)

    arr.sort()
    low = 0
    high = k
    total = 0
    while high < len(arr):
        curr = arr[high]
        while (high < len(arr) - 1) and (curr // 10 == arr[high + 1] // 10):
            high += 1
        total += sum(arr[low : high + 1])
        low = high + 1
        high += k - (high - low)
    return total
