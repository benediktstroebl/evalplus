
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
    # Initialize the sum to 0
    result = 0

    # Iterate through the first k elements of the array
    for i in range(min(k, len(arr))):
        # Convert each element to a string and check if it has two digits or less
        if len(str(arr[i])) <= 2:
            # If the element has two digits or less, add it to the sum
            result += arr[i]

    # Return the sum
    return result

