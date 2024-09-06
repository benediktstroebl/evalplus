
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
    # 堆排序，O(n+klog(n))
    if len(arr) <= k:
        return sorted(arr, reverse=True)
    # 创建一个堆
    heap = arr[:k]
    heapq.heapify(heap)
    # 遍历剩余的元素
    for i in range(k, len(arr)):
        # 堆顶元素小于最后一个元素，则交换，并调整堆
        if heap[0] < arr[i]:
            heapq.heappushpop(heap, arr[i])
    # 返回一个按从大到小排列的 k 个数
    return heap

