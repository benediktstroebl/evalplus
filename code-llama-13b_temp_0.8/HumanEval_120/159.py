
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
    # 思路1：用python内置的heapq模块找前k个最大的元素
    # import heapq
    # heapq.nlargest(k, arr)

    # 思路2：使用快排
    # 快排思想：选择一个基准元素，排序基准元素左边的元素比它小，右边的比它大
    # 比它大的元素进行左右分割，递归处理
    # 缺陷：
    # 1. 会有不同的基准元素选取方法，难以确定稳定性
    # 2. 快排的空间复杂度不好控制
    # 3. 需要改写
    def _partition(arr, left, right):
        # 设置基准元素，选取最右端的元素
        pivot = arr[right]
        # 记录左分割点
        # i作为左分割点，在循环中，每次遇到比基准元素小的就把它放在i的位置上，而i依次向后移动
        i = left - 1
        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                # 交换位置
                arr[i], arr[j] = arr[j], arr[i]
        # 把基准元素放在分割点
        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i+1
    def _quick_sort(arr, left, right):
        if left < right:
            mid = _partition(arr, left, right)
            _quick_sort(arr, left, mid-1)
            _
