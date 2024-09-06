
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
    # Runtime: 44 ms
    # Memory: 14.1 MB
    two_digits = [i for i in arr[:k] if i >= 10 and i <= 99]
    one_digit = [i for i in arr[:k] if i >= 1 and i <= 9]
    return sum(two_digits) + sum(one_digit)
