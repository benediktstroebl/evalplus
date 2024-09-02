
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
    # Sum the numbers that have at most 2 digits
    # A number is considered having 2 digits if the first digit is non-zero
    # and the number of digits is at most 2
    # So sum everything starting from index 0 to k-1, but only sum if the first digit is non-zero

    k = min(len(arr), k) # make sure we don't index out of bounds
    total = 0

    for i in range(k):
        # Get the first digit of the number
        first = arr[i] // 10
        if first != 0:
            total += arr[i]

    return total
