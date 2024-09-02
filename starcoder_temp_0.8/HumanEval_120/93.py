
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
    # M1. 冒泡排序 O(nlogn)
    #     稳定排序，把数组看做k+1个数，最后的k个数即为最大的k个数。
    #     即遍历每个数，与后面最大的k-1个数比较，替换后面最大的k-1个数。
    #     时间复杂度分析：
    #         每次遍历至少要和后面的一个最大数进行比较，因此总共要执行(n-1)*k次比较，故时间复杂度为O(n)。
    #         由于每次遍历只需要和后面的一个最大数进行比较，所以可以认为是稳定的。
    #
    # arr.sort()
    # return arr[-k:]

    # M2. 堆排序 O(nlogk)
    #     堆排序是一种稳定的排序方法，它的时间复杂度是 O(nlogk)。
    #     堆排序的思想是：建立大顶堆，把最大的 k 个元素放到堆顶，然后把堆顶元素与堆的最后一个元素交换，
    #     然后把堆的元素重新调整为堆，如此反复，直到把所有元素放到堆中。
    #
    # heap = []
    # for i in range(k):
    #     heapq.heappush(heap, arr[i])
    # for i in range(k, len(arr)):
    #     if arr[i] > heap[0]:
    #         heapq.heappop(heap)
    #         heapq.heappush(heap, arr[i])
    # return heap

    # M3. 分治算法 O(nlogk)
    #     分治算法是一个递归算法，它的步骤如下：
    #     1. 数组的规模被分成n/2和n-n/2两个规模，递归执行分治算法；
    #     2. 如果当前数组的规模为n/2，则利用分治算法求解；
    #     3. 如果当前数组的规模为n-n/2，则利用分治算法求解；
    #     4. 将步骤1、2、3的结果合并。
    #
    # 时间复杂度分析：
    #     分治算法的时间复杂
