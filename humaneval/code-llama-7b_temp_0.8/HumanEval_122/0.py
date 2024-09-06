
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

    # sum the first k elements
    sum = 0
    for i in range(k):
        sum += arr[i]

    # remove the first k elements
    arr = arr[k:]
    # remove the first element
    arr = arr[1:]
    # remove the first element
    arr = arr[1:]

    return sum + add_elements(arr, 1)

