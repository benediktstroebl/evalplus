
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
    first_k = arr[:k]
    first_2_digit_sum = sum(e for e in first_k if 9 < e < 100)
    first_1_digit_sum = sum(e for e in first_k if e < 10)

    return first_2_digit_sum + first_1_digit_sum

