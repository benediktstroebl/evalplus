
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
    def two_digits(x):
        """
        A function to determine if the number has less than or two digits
        """
        return len(str(x)) <= 2

    result = 0
    for index, item in enumerate(arr):
        if index == k:
            break
        if two_digits(item):
            result += item
    return result

