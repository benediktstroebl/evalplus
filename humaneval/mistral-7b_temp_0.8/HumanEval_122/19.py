
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

    # Return the sum of the first k elements of arr,
    # with at most two digits.
    # If k is 1, return the first element of arr.
    # If k is 2, return the sum of the first two elements of arr.
    # If k is 3, return the sum of the first three elements of arr.
    # If k is 4, return the sum of the first four elements of arr.
    # If k is 5, return the sum of the first five elements of arr.
    # If k is 6, return the sum of the first six elements of arr.
    # If k is 7, return the sum of the first seven elements of arr.
    # If k is 8, return the sum of the first eight elements of arr.
    # If k is 9, return the sum of the first nine elements of arr.
    # If k is 10, return the sum of the first ten elements of arr.

    return sum(arr[:k])
