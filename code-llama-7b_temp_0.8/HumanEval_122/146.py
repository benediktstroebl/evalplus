
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
    max_n = 10
    count = 0
    # assume that the first k elements must be in the result
    for i in range(k):
        count += arr[i]

    # find the sum of k + 1 ... n
    for j in range(k, len(arr)):
        if count >= 10:
            count -= max_n
        count += arr[j]

    return count
