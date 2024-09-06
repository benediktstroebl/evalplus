
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
    # if arr is empty return 0
    if not arr:
        return 0

    # if k is 0 return the sum of arr
    if k == 0:
        return sum(arr)

    # if k is 1, sum of 1st and remaining elements
    if k == 1:
        return sum(arr[:2]) + sum(arr[2:])

    # if k is 2, sum of first and 2nd elements
    if k == 2:
        return sum(arr[:2]) + sum(arr[2:3]) + sum(arr[3:])

    # if k is 3, sum of first and 2nd and 3rd elements
    if k == 3:
        return sum(arr[:2]) + sum(arr[2:3]) + sum(arr[3:])

    # if k is not 0, sum of first and 2nd, 3nd and remaining elements
    return sum(arr[:2]) + sum(arr[2:3]) + sum(arr[3:])

