
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
    # total = 0
    # for i in range(len(arr)):
    #     if i < k:
    #         total += arr[i]
    # return total

    # O(n) solution
    two_digits = set(str(i) for i in range(10, 100))
    total = 0
    for i in range(k):
        if str(arr[i]) in two_digits:
            total += arr[i]
    return total
