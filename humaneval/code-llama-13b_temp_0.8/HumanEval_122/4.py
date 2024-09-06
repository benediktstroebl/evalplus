
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
    # 0 <= k <= len(arr)
    if k > len(arr):
        return 0
    # 1 <= k <= len(arr)
    elif k <= 0:
        return 0

    result = 0
    for elem in arr[:k]:
        # 1 <= n <= 99
        if elem < 100 and elem > 9:
            # 10 <= n <= 99
            elem = elem // 10
            result += elem
        elif elem < 10:
            # 0 <= n <= 9
            result += elem
    return result

