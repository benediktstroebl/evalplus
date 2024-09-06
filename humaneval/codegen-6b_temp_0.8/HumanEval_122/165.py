
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
    max_n = k if k > 0 else len(arr)
    m = 10**(len(str(max_n)) - 1)
    # use 2 digit numbers
    arr = [int(x) for x in arr]
    _sum = sum(x for x in arr[:max_n])
    # multiply by 10**(len(str(max_n)) - 1)
    return _sum * m
