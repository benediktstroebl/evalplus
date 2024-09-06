
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
    # Check if k is less than 1
    if k < 1:
        return 0

    # Check if the array is empty
    if not arr:
        return 0

    # Check if k is equal to the length of the array
    if k == len(arr):
        return sum(arr)

    # Check if the length of the array is greater than k
    if len(arr) > k:
        return 0

    # Initialize the variable
    sum = 0

    # Loop through the first k elements of the array
    for i in range(max(1, k)):
        sum += arr[i]

    return sum