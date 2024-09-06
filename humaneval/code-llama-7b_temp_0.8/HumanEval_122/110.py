
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
    """
    Runtime: 208 ms, faster than 75.73% of Python3 online submissions for Sum of Digits of the Minimum Number.
    Memory Usage: 13.6 MB, less than 28.98% of Python3 online submissions for Sum of Digits of the Minimum Number.
    """
    first_k_numbers = arr[:k]
    return sum([int(str(number)[:2]) for number in first_k_numbers])

