
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
    """
    Time: O(N), for each element, need to check if have two digits
    Space: O(N), for storing elements
    """
    two_digits_sum = 0
    arr_len = len(arr)
    if arr_len > k:
        arr = arr[:k]

    for num in arr:
        if len(str(num)) <= 2:
            two_digits_sum += num

    return two_digits_sum

