
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
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    for i in range(k):
        if len(str(arr[i])) <= 2:
            return str(arr[i])
    return 0
arr = [2,3,4,5,6,7,8,9,10]
