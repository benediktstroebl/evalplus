
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
    # Edge case when k is greater than or equal to len(arr)
    if k >= len(arr):
        return sum(arr)

    # Initialize sum as 0
    sum = 0

    # Iterate over arr[0:k] and add the elements to sum
    for i in arr[0:k]:
        sum += i

    # Return the sum of elements with at most two digits
    return sum

