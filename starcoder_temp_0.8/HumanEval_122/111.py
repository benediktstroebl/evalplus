
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
    n = len(arr)
    max_sum = -100000
    cur_sum = 0
    for i in range(k):
        cur_sum += arr[i]
    max_sum = max(max_sum, cur_sum)
    i, j = 0, k
    while j < n:
        cur_sum += arr[j] - arr[i]
        max_sum = max(max_sum, cur_sum)
        i += 1
        j += 1
    return max_sum

