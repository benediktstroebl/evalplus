
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

    # Check if k is greater than the length of the array
    if k > len(arr):
        return 0

    # Initialize the result variable
    result = 0

    # Loop through the first k elements of the array
    for i in range(k):
        # Check if the element has at most two digits
        if len(str(arr[i])) <= 2:
            # Add the element to the result
            result += arr[i]

    # Return the result
    return result