
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
    # Check for empty array
    if len(arr) == 0:
        return 0
    # Check for no digits in the first k elements of arr
    k2 = 0
    while k2 < k and not any(str(i).isdigit() for i in arr[:k2+1]):
        k2 += 1
    # Check for overflow
    if k2 >= len(arr):
        return 0
    # Get the sum
    sum = 0
    for i in arr[:k2+1]:
        sum += int(i)
    return sum