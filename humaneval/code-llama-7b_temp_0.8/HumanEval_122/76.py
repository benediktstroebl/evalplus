
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
    if not arr or len(arr) == 0: return 0
    if k > len(arr): k = len(arr)
    total = 0

    for idx, val in enumerate(arr[:k]):
        # counting the number of digits of the current value
        num_of_digits = 0
        while val > 0:
            num_of_digits += 1
            val //= 10
        
        if num_of_digits <= 2:
            total += val

    return total
