
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

    # We're keeping track of the sum of elements with at most 2 digits
    # i.e. sum(arr[:k]) if arr[:k] has elements with at most 2 digits.
    # Initially, this value is zero because arr[:k] does not have any elements
    # with at most 2 digits.
    sum_of_elements = 0

    # Iterate through the first k elements of arr
    for i in range(k):
        # For each element of arr[:k], we check whether its
        # value is within the range 1 <= value <= 99.
        # If the element's value is within this range,
        # we update sum_of_elements by adding the element's value
        # to it.
        if 1 <= arr[i] <= 99:
            sum_of_elements += arr[i]

    # We return sum_of_elements as our final answer
    return sum_of_elements
