
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
    n = len(arr)
    k = max(k, 0)
    # 将arr按照大小进行排序
    arr.sort()
    # 将最小值和最大值作为最后两个元素，保留一个空位
    arr = [arr[0], arr[-1], arr[-1]]
    for i in range(k-1, -1, -1):
        # 找到k个最大的元素，并移除它们
        j = n-k+1
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1]