
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
    if not arr:
        return None

    if k == 0:
        return 0

    result = 0
    for i in range(0, k):
        result += arr[i]

    result -= (10 * k)

    if result > 100:
        result %= 100
    elif result < 0:
        result = 100 - abs(result)

    return result

