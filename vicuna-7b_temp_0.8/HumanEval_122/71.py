
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
    # Step 1: count the sum of the digits from 1 to k
    digits = 0
    for i in range(1, k+1):
        digits += int(arr[i])

    # Step 2: add the sum of the elements with at most two digits from the first k elements of arr
    return digits + sum(arr[i:i+2] for i in range(0, len(arr), 2) if i+2 <= k)
