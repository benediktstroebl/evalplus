
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
    n = len(arr)
    if n == 0:
        return 0
    if k == 0:
        return 0
    if k >= n:
        return 0
    max_digit = max(map(int, str(arr[0]).split('')))
    max_sum = 0
    if max_digit < 10:
        max_sum = max_digit * 10 + 1
    for i in range(1, n):
        sum = 0
        for j in range(1, max_digit + 1):
            digit = int(arr[i] / j)
            if digit > 0:
                sum += digit * j
        max_sum = max(max_sum, sum)
    return max_sum