
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
    k_elms = 0
    s = 0
    for elm in arr:
        if elm < 10:
            s += elm
        elif elm < 100:
            s += elm
        else:
            k_elms += 1
            if k_elms <= k:
                s += elm % 10
                s += elm // 10 % 10
    return s

