
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
    total_sum = 0
    valid_idx = 0
    while valid_idx < k:
        total_sum += arr[valid_idx]
        valid_idx += 1

    accumulator = 0

    for i in range(k, len(arr)):
        accumulator += arr[i]
        if arr[i] < 10:
            accumulator -= arr[i - k]

        if accumulator <= 0:
            break
    return total_sum + accumulator

