
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
    # On a scale of 0 to 1000, what is the sum of the elements with at most two digits from the first k elements of arr?
    # Return this sum.

    # O(n)
    # 128ms, 100%
    def two_digit_sum(digits):
        if digits < 10:
            return digits
        return digits - 10 + digits // 10

    if k > len(arr):
        k = len(arr)

    # Pythonic way to do two_digit_sum
    def two_digit_sum(digits):
        return min(digits % 100, digits)

    # O(k)
    # 108ms, 100%
    # return sum(map(two_digit_sum, arr[:k]))

    total = 0

    for index, value in enumerate(arr[:k]):
        total += min(value % 100, value)

    return total
