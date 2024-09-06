
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
    # step 1: make sure we have enough elements to actually do this summing
    if len(arr) <= k:
        return sum(arr)

    # step 2: find the numbers that have more than two digits in them
    count = 0
    for num in arr[:k]:
        if len(str(num)) > 2:
            count += 1

    # step 3: add the values of all elements in the first k - count elements
    return sum(arr[:k - count])
