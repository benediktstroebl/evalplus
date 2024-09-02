
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
    m = 100

    def two_digits_from_left(i, j):
        digits = []
        for idx in range(i, j + 1):
            digits.append(arr[idx] % m)
            arr[idx] //= m
        return sum(digits)

    def two_digits_from_right(i, j):
        digits = []
        for idx in range(j, i - 1, -1):
            digits.append(arr[idx] % m)
            arr[idx] //= m
        return sum(digits)

    def get_sum_with_two_digits(i, j):
        if i == j:
            return 0
        return two_digits_from_left(i, j) + two_digits_from_right(i, j)

    l = 0
    r = len(arr) - 1
    res = 0
    while l < r:
        res += get_sum_with_two_digits(l, min(l + k - 1, r))
        if l + k - 1 <= r:
            l += k
        else:
            r -= k
    res += get_sum_with_two_digits(l, r)
    return res

