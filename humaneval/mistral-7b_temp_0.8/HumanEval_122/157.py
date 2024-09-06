
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

    """
    The solution is to use two variables, one for the first k elements and
    one for the remaining elements. Each time we add a new element, we add
    it to the appropriate variable.
    """

    # Store the first k elements
    first_k = arr[:k]

    # Store the remaining elements
    remaining = arr[k:]

    # Initialize the sum of the first k elements
    sum_first_k = 0

    # Iterate through the first k elements
    for i in first_k:
        # If the element has two or fewer digits, add it to the sum
        if len(str(i)) <= 2:
            sum_first_k += i

    # Initialize the sum of the remaining elements
    sum_remaining = 0

    # Iterate through the remaining elements
    for i in remaining:
        # If the element has two or fewer digits, add it to the sum
        if len(str(i)) <= 2:
            sum_remaining += i

    # Return the sum of the first k elements and
