
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
    arr_res = []

    def dfs(arr, k):
        if not arr or len(arr_res) >= k:
            return

        cur_max, cur_max_index = float('-inf'), -1
        for i in range(len(arr)):
            if arr[i] > cur_max:
                cur_max = arr[i]
                cur_max_index = i

        arr_res.append(arr[cur_max_index])
        arr.remove(cur_max)
        dfs(arr, k)

    dfs(arr, k)
    return arr_res

