
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

    # Edge case
    if len(arr) == 0 or k <= 0 or len(arr) < k:
        return -1

    # Loop through the array
    k_sum = 0
    for i in range(k):
        k_sum += arr[i]

    # Initialize a variable to hold the count
    # of elements with at most 2 digits
    two_digit_count = 0

    # Loop through the array
    for i in range(k, len(arr)):
        # Add the next element
        k_sum += arr[i]

        # If the sum is now 2 digits, increment the count
        if k_sum > 99:
            two_digit_count += 1

        # If the sum is now 1 digit, reset the sum
        elif k_sum < 10:
            k_sum = arr[i]

    # Return the count
    return two_digit_count
