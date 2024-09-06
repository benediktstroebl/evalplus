
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
    # 1 <= len(arr) <= 100
    if len(arr) < 2:
        return sum(arr[:k])

    # k is less than or equal to the len(arr)
    if k > len(arr):
        k = len(arr)

    result = 0
    # all the elements in the array
    for idx, item in enumerate(arr):
        # if the index is less than or equal to k
        if idx <= k:
            # get the last two digits
            digit = item % 100
            # add the number
            result += digit

    return result

