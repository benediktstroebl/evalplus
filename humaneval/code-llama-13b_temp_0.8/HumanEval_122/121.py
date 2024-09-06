
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

    if not arr:
        return 0

    # binary search for the largest element
    # find the length of the integer
    n = len(str(max(arr[:k])))

    # check if the length of the integer is greater than 2
    if n > 2:
        return 0

    # reduce the list size to n
    arr = arr[:k]

    # sort the list
    arr = sorted(arr, reverse=True)

    # iterate the list
    sum = 0
    for i in range(n):
        sum += arr[i]

    return sum

