
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
    k -= 1

    def helper(arr, k):
        if not arr:
            return 0
        elif k == 0:
            return arr[0]
        else:
            return max(arr[0] + helper(arr[1:], k - 1), helper(arr[1:], k))

    return helper(arr, k)

