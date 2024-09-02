
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
    # Note: This is a "hard mode" variant of the basic "two sums" problem,
    # see 001-two-sum.py for a solution to that version.

    # To solve this problem, we need to write a simple, recursive algorithm that
    # iterates over the array arr, counting the sum as it goes. The tricky part
    # here is that we only want to count sums of elements up to two digits.
    # We can do this by limiting our iteration to the first k elements of the
    # array and then stopping if the sum is greater than 99.

    return sum(arr[:k]) if sum(arr[:k]) < 100 else sum(arr[:k]) - 9 * (k - 1)
