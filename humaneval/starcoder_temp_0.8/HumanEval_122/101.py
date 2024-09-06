
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
    # Store the element with less than or equal to two digits from the first k elements
    store = set()

    # Loop over the first k elements
    for i in range(k):
        # If the element has less than or equal to two digits
        if len(str(arr[i])) <= 2:
            # Add it to the store
            store.add(arr[i])

    # Return the sum of the elements with at most two digits from the first k elements
    return sum(store)

