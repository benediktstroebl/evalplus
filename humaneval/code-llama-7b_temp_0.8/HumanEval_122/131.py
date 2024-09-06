
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
    if k == 0:
        return 0

    # The two digits sum is calculated using the sum of the 
    # digits of the two closest numbers, the distance between
    # them is at most one.
    two_digits_sum = 0
    one_digit_sum = 0
    digit_sum = 0
    for i in range(k):
        digit_sum += arr[i]

    if k >= 2:
        two_digits_sum = digit_sum % 100
        one_digit_sum = digit_sum % 10

    for i in range(k, len(arr)):
        digit_sum = digit_sum - arr[i - k] + arr[i]
        if k >= 2:
            two_digits_sum = max(digit_sum % 100, two_digits_sum)
            one_digit_sum = max(digit_sum % 10, one_digit_sum)
        if k >= 1:
            one_digit_sum = max(digit_sum % 10, one_digit_sum)
    if k >= 2:
        return two_digits_sum
    elif k >= 1:
        return one_digit_sum
