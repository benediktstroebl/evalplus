
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
    # O(n) time | O(n) space
    # 1 <= arr <= 1000
    if len(arr) == k:
        return sum(arr)

    arr_sum = 0
    for i in range(min(k, len(arr))):
        # Keep it under 100
        if arr[i] > 99:
            break

        arr_sum += arr[i]

    return arr_sum

