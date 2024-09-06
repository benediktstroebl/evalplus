
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
    #
    #     # Brute force solution
    #     res = []
    #     for i in range(k):
    #         if len(str(arr[i])) <= 2:
    #             res.append(arr[i])
    #     return sum(res)
    #
    # # Approach 1:
    #     return sum(arr[i] for i in range(k) if len(str(arr[i])) <= 2)
    #
    # # Approach 2
    # arr = sorted(arr[:k], key=len)
    # return sum(arr)
    #
    # # Approach 3
    # res = []
    # for i in range(k):
    #     if len(str(arr[i])) <= 2:
    #         res.append(arr[i])
    # return sum(res)

    # Approach 4
    max_len = 0
    for i in range(k):
        max_len = max(max_len, len(str(arr[i])))

    total = 0
    for i in range(k):
        if len(str(arr[i])) <= max_len:
            total += arr[i]
    return total
