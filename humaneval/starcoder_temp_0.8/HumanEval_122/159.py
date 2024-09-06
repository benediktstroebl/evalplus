
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
    def get_sum(arr, k):
        m = 10
        n = 99
        ans = 0
        for i in range(k):
            ans += m * (arr[i] // 10) + arr[i] % 10

        for i in range(k, len(arr)):
            m, n = n, n + 10
            ans += m * (arr[i] // 10) + arr[i] % 10

        return ans

    # #method 1
    # if len(arr) > k:
    #     k_max = arr[k - 1] // 10
    #     k_min = arr[k - 1] % 10
    #     for i in range(k, len(arr)):
    #         if k_max * 10 + k_min < arr[i]:
    #             k_max, k_min = arr[i] // 10, arr[i] % 10
    #     return k_max * 10 + k_min
    # else:
    #     return get_sum(arr, k)

    # #method 2
    return get_sum(arr, k)

