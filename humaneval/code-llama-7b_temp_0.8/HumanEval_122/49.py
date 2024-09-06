
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
    # Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
    # Output: 24 # sum of 21 + 3
    # [111,21,3,4000,5,6,7,8,9]
    # [111,21,3,4000,5]
    # [111,21,3,4000]
    # [111,21,3]
    # [111,21]
    # [111]
    if k == 1:
        return sum(arr[0:k])

    if k == 2:
        return sum(arr[0:k]) + min(arr[0:2])

    if k >= len(arr):
        return sum(arr[0:len(arr)])

    return sum(arr[0:k]) + min(arr[k-2:k]) + min(arr[0:k-2])

    # Solution 1: Time O(n) - Space O(1)
    # if k > len(arr):
    #     return sum(arr)

    # if k <= 2:
    #     return sum(arr[0:k])

    # return sum(arr[0:k]) + min(arr[k-2:k]) + min(arr[0:k-2])

    # if k > len(arr):
    #     return sum(arr)

    # if k <= 2:
    #     return sum(arr[0:k])

    # return sum(arr[0:k]) + min(arr[k-2:k]) + min(arr[0:k-2])

    # Solution 2: Time O(n) - Space O(n)
    # if k > len(arr):
    #     return sum(arr)

    # if k <= 2:
    #     return sum(arr[0:k])

    # return sum(arr[0:k]) + min(arr[k-2
