
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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    two_digits = 0
    for i, num in enumerate(arr):
        if num < 10:
            two_digits += num
        elif num < 100:
            two_digits += num
        else:
            break
        if i == k:
            break
    return two_digits
