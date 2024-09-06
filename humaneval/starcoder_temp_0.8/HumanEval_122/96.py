
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
    # init
    result = 0
    # iterate through array
    for i in range(k):
        # sum up elements with 2 or 1 digits
        if arr[i] < 10:
            result += arr[i]
        elif 10 <= arr[i] <= 99:
            result += arr[i]
    return result
