
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
    # MAX_ELEMENT = 99
    # MAX_TWO_DIGITS = 99
    MAX_TWO_DIGITS = 99
    MAX_ELEMENT = 999

    prefix = [0] * len(arr)
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    two_digits_sums = [0] * (k + 1)
    two_digits_sums[0] = 0
    for i in range(1, k + 1):
        two_digits_sums[i] = two_digits_sums[i - 1]
        if arr[i - 1] <= MAX_TWO_DIGITS:
            two_digits_sums[i] += arr[i - 1]

    ans = 0
    for i in range(k, len(arr)):
        ans += prefix[i] - prefix[i - k]
        if arr[i] <= MAX_TWO_DIGITS:
            ans -= two_digits_sums[k] - two_digits_sums[i - k]

    return ans

