
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
    if len(arr) <= 100:
        arr = [abs(x) if x >= 0 else -x for x in arr] # convert to absolute value if negative
        left = max(0, len(arr) - k)
        left = left + 1 if not arr[left] % 100 in ['1', '3', '7', '9'] else left
        right = min(len(arr), max(k, len(arr) - left + 1, 10))
        result = 0
        for i in range(left, right):
            result = result + arr[i]
        return result
    return 0

