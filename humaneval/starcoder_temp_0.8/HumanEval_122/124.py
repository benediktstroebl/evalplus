
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

    if len(arr) <= 0 or len(arr) <= k:
        return 0
    if k == 1:
        return 0
    if k == 2:
        return arr[0] + arr[1]

    carry = 0
    result = 0
    i = 0
    while i < k:
        result += arr[i]
        if carry > 0:
            result += carry
        if result > 99:
            result = result % 100
            carry = 1
        else:
            carry = 0
        i += 1

    return result
