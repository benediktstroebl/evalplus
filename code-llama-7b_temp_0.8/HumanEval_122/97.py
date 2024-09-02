
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
    def at_most_two(num):
        digits = [int(n) for n in str(num)]
        if len(digits) == 1 or len(digits) == 2:
            return sum(digits)
        else:
            return 0
    return sum(map(at_most_two, arr[:k]))
