
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
    arr = sorted(arr)
    n = 0
    for i in range(k):
        n += arr[i]
    for i in range(k+1, len(arr)):
        n += arr[i] if len(str(arr[i])) <= 2 else 0
    return n
