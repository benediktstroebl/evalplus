
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

    # 使用 堆排序 来解决此题
    # 维护一个大小为 k 的堆，将数组的前 k 个元素压入堆中
    # 剩余元素依次与堆顶元素比较，如果比堆顶元素大，则替换堆顶元素
    # 堆中存放的是 arr 数组的索引

    import heapq
    indices = [i for i, _ in enumerate(arr)]
    heapq.heapify(indices)

    res = [0] * k
    for i in range(k):
        res[i] = arr[indices[0]]
        heapq.heapreplace(indices, heapq.heappop(indices))
    return res

