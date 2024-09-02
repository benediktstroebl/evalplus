
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
    if k < 1:
        return 0
    if k >= len(arr):
        return sum(arr)

    total = 0
    for i in range(k):
        el = arr[i]
        if el < 10:
            total += el
        elif el < 100:
            total += el
        else:
            total += el % 10
            total += el // 10

    return total

