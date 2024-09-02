
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
    # For each value in the array
    # check if the value is less than 10
    # and add it to the sum if it is
    # Otherwise check if the value is less
    # than 100 and add it to the sum if it is
    result = 0
    for idx in range(k):
        value = arr[idx]
        if value < 10:
            result += value
        elif value < 100:
            result += value
    return result

