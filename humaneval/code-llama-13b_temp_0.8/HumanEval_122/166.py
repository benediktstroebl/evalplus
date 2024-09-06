
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
    def two_digit_sum(x):
        """
        Returns the sum of digits of x if x has two digits, else 0.
        """
        if x < 10:
            return 0
        if x < 100:
            return sum(int(i) for i in str(x))
        else:
            raise ValueError("x must be two digits")
    return sum(two_digit_sum(x) for x in arr[:k])

