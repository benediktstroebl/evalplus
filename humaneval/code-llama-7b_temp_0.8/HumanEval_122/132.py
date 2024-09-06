
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
    # "self": O(n) time | O(n) space
    # "two pointers": O(n) time | O(1) space
    if k == 0: return 0

    self = 0
    for el in arr[:k]: self += el

    two_pointers = 0
    for i in range(k, len(arr)):
        two_pointers = two_pointers - int(str(arr[i-k])[-1]) + int(str(arr[i])[-1])
        self += two_pointers

    return self
