
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
    # def find_min(arr):
    #     for i, n in enumerate(arr):
    #         if n >= 10:
    #             return i
    #     return len(arr)

    # min_index = find_min(arr)

    # arr = arr[:min_index]

    # if len(arr) < k:
    #     return 0

    # arr.sort()
    # s = sum(arr[:k])

    # return s

    # res = 0

    # for i in range(k):
    #     if arr[i] < 10:
    #         res += arr[i]
    #     elif arr[i] < 100:
    #         res += arr[i] // 10

    # return res

    return sum(i for i in arr[:k] if i < 10 or i < 100)
