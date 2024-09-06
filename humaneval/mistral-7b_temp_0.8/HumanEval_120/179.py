
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

    res = []
    n = len(arr)
    for i in range(k):
        # 记录最大数的下标
        max_index = i
        # 遍历找最大值
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # 把最大值加入结果集
        res.append(arr[max_index])
        # 删除最大值
        arr.remove(arr[max_index])

    return res

