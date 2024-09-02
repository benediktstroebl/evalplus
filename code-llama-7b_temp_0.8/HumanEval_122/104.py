
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
    # check the first k elements for at most 2 digits
    sum_ = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_ += arr[i]

    # check the rest of the elements for at most 2 digits
    for i in range(k, len(arr)):
        if len(str(arr[i])) <= 2:
            sum_ += arr[i]

    return sum_

    # # k = min(k, len(arr))
    # # d = {}

    # # for i in range(k):
    # #     if len(str(arr[i])) <= 2:
    # #         d[arr[i]] = d.get(arr[i], 0) + 1

    # # for i in range(k, len(arr)):
    # #     if len(str(arr[i])) <= 2:
    # #         d[arr[i]] = d.get(arr[i], 0) + 1

    # # return sum(d.keys())

