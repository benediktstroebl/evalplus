
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
    if k == 0:
        return 0
    elif k == 1:
        return sum(arr)
    elif k == 2:
        return sum([i * 10 + j for i, j in zip(arr[:2], arr[2:])])
    else:
        return sum([i * 10 + j for i, j in zip(arr[:k-1], arr[k-1:])]) + add_elements(arr, k-1
