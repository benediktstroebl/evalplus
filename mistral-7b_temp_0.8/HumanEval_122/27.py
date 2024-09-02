
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
    # Return the sum of the integers in arr whose digits are less than or equal to k.
    # We start by initializing a sum variable to 0.
    # We then iterate through the elements of arr, and if the current element's digits are less than or equal to k, we add it to the sum.
    # Finally, we return the sum.
    sum_ = 0
    for num in arr:
        if len(str(num)) <= k:
            sum_ += num
    return sum_
