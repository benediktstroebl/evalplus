
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
    # 堆排序
    # 堆排序是指利用堆这种数据结构实现排序的算法。
    # 堆是一种近似完全二叉树的结构（通常堆是通过一维数组来实现的），
    # 它的特点是：除叶子节点外，每个父节点的值都是大于或小于（取决于堆类型）叶子节点的值。
    # 大根堆： 父节点的值都是大于叶子节点的值；
    # 小根堆： 父节点的值都是小于叶子节点的值。
    # 排序思路：利用堆排序思想，将数组首位元素放入堆中，然后从堆中取出最大（或小）的元素放入输出数组中，
    # 然后将堆中最后一个元素放入堆中，再取出堆中最大（或小）的元素放入输出数组中，以此类推，直到堆中没有元素。
    if len(arr) == k:
        return arr
    heapq.heapify(arr)
    res = []
    for _ in range(k):
        res.append(heapq.heappop(arr))
    return res

