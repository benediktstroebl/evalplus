
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
    def _add_numbers(num):
        """
        Returns sum of digits in `num`.
        """
        return sum([int(n) for n in str(num)])

    def _within_two_digits(num):
        """
        Returns True if number has two or fewer digits.
        """
        return True if len(str(num)) <= 2 else False

    total = 0
    # Return sum of first k elements if all elements have <= 2 digits.
    if len(arr) >= k and all([_within_two_digits(n) for n in arr[:k]]):
        return sum(arr[:k])

    # Iterate over elements in `arr`.
    for n in arr:
        # If number has <= 2 digits, add to `total`.
        if _within_two_digits(n):
            total += n
        # If number is larger than 2 digits, add sum of its digits to `total`.
        else:
            total += _add_numbers(n)
        # If `total` is greater than k, return total.
        if total > k:
            return total

    return total

