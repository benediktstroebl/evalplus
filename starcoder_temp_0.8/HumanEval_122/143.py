
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

    arr_len = len(arr)

    if arr_len <= k:
        return sum(arr)

    carry = 0
    result = 0

    for i in range(k):
        result += arr[i]

    for j in range(k, arr_len):
        result += arr[j]
        carry += arr[j]

    while carry > 0:
        result += carry % 10
        carry //= 10

    return result
