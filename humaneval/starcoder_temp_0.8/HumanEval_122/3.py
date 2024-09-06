
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
    def helper(arr, k, idx, s):
        if k == 0:
            return s
        if len(arr[idx]) <= 1:
            return helper(arr, k-1, idx+1, s+int(arr[idx]))
        else:
            return helper(arr, k-1, idx+1, s+int(arr[idx][0]))

    return helper(arr, k, 0, 0)

