
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
    # Make sure the input is not empty
    if not arr:
        return 0

    # Create a copy of the input array
    arr = [x for x in arr]

    # Initialize the sum to 0
    sum = 0

    # Loop through the first k elements of the array
    for i in range(k, len(arr)):
        # Keep track of the sum of the elements with two digits
        sum += arr[i]

        # Keep track of the last digit of the sum
        last_digit = sum[-1]

        # If the last digit is a 0, reset the sum to 0
        if last_digit == '0':
            sum = 0

    # Return the sum of the elements with at most two digits
    return sum
