
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
    _min = float("inf")
    _max = float("-inf")
    ans = 0

    for i in range(len(arr)):
        if i == k:
            break

        if _min <= arr[i] <= _max:
            ans += arr[i]

        if arr[i] > _max:
            _max = arr[i]
        elif arr[i] < _min:
            _min = arr[i]

    return ans
