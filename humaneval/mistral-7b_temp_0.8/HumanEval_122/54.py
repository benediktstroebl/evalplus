
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
    # get the sum of the first k elements
    # filter the list of sum of first k elements based on whether there are at most 2 digits
    # loop through the list and add the elements whose value is < 100
    # return the sum
    return sum(
        [
            num
            for num in arr[:k]
            if len(str(num)) <= 2
        ]
    )
