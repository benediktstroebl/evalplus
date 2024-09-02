
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
    if len(arr) < k+1:
        return 0
    else:
        n = 1
        arr = sorted(arr)
        for i in range(1, k+1):
            n *= i
            if n > len(arr):
                break
        if len(arr) % n != 0:
            n += 1
        return sum(arr[:n])