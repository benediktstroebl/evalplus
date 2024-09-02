
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
    # Subtract the kth element from every element in the array.
    # Sort the elements in ascending order.
    # Make the sum of the first k elements, excluding the kth element,
    # and return the sum.
    if k == 0:
        return 0
    if len(arr) == k:
        return sum(arr)
    return sum(sorted(arr)[:k]) - arr[k]
