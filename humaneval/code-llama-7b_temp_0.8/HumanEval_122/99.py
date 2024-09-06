
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

    # creates empty array to store sums
    sums = []

    # loop through the array starting at k
    for i in range(k, len(arr)):
        # create a sum
        sum = 0
        # loop through the first k elements
        for j in range(i - k, i):
            # add the numbers to the sum
            sum += arr[j]
        # add the sum to the sums array
        sums.append(sum)

    # return the sums array
    return sums
