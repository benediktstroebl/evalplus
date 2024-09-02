
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

    # sort the array
    arr.sort()

    # use two pointers to iterate through the sorted array
    i = 0
    j = 0
    while j < k:
        if len(str(arr[i])) <= 2:
            sum += arr[i]
        j += 1
        i += 1

    return sum



