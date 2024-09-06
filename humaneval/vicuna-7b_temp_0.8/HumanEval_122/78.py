
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
    left = k*10
    right = len(arr) * 10
    sum = 0
    for i in range(k, len(arr)):
        digit = arr[i] // 10
        if digit == 1 or digit == 2:
            sum += digit * (right - left)
        left = digit * 10
    return sum
