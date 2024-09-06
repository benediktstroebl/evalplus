
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

    # If k is bigger than the size of the array, then we just
    # return the sum of the array.
    if k >= len(arr):
        return sum(arr)

    sum = 0

    # for each number in the array, sum up the numbers
    for i in range(len(arr)):

        # if the number is bigger than two digits, we skip it.
        if len(str(arr[i])) > 2:
            continue

        sum += arr[i]

    return sum

