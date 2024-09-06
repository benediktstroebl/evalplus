
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
    # initialize the result to 0
    result = 0

    # loop through the first k elements of arr
    for i in range(k):
        # if the current element has more than two digits, add it to the result
        if len(str(arr[i])) > 2:
            result += arr[i]

    # return the result
    return result