
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    ans = []
    if k > len(arr):
        return ans
    def find_maximum(arr, k):
        if k == 0:
            return []
        ind = n // k
        left, right = -inf, inf
        while left < right:
            mid = (left + right) // 2
            cur_ind = k - 1
            if (arr[(ind + cur_ind) % n] > mid):
                left = mid
            else:
                right = mid
        return left
    for i in range(k):
        left, right = -inf, inf
        for j in range(n):
            if arr[j] > left:
                left = arr[j]
            if arr[j] > right:
                right = arr[j]
        ans.append(left if left != -inf else right)
        arr.remove(left if left != -inf else right)
    return ans
