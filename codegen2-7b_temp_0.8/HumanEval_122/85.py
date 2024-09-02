
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

    s = 0
    for i in range(k):
        s += arr[i]

    result = int(str(s)[0:2] + str(s)[2:])

    return result if result <= 10**2 else add_elements(arr[1:], k)

