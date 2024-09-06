
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

    if k > len(arr):
        return 0

    # 0 <= arr[i] <= 999
    # len(arr) <= 100
    result = 0
    for i in range(k):
        # 0 <= digit <= 9
        digit = arr[i] % 10
        result += digit

        # 0 <= digit <= 9
        digit = (arr[i] % 100) // 10
        if digit:
            result += digit

    return result

