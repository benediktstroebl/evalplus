
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
    bitmap = 0
    for num in arr[:k]:
        bitmap = (bitmap << 10) + num

    result = bitmap
    for num in arr[k:]:
        bitmap = 0
        for i in range(10):
            bitmap += ((num >> i) & 1) * (bitmap << i)
        result += bitmap

    return result
