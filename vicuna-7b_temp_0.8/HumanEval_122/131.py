
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
    # check if the input is valid
    if len(arr) < 1 or len(arr) > 100 or k < 1 or k > len(arr):
        return -1

    # get the sum of digits
    sum = 0
    for i in arr[:k]:
        sum += i

    # check if the input is valid
    if sum > 99:
        return -1

    # return the sum
    return sum
