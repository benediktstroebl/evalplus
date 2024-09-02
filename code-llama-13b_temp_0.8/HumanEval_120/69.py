
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
    # 1st approach: O(nlogn)
    # n = len(arr)
    # m = k if n > k else n
    # # O(mlogm)
    # heap = sorted(arr, reverse=True)[:m]
    # # O(mlogn)
    # heapq.heapify(heap)
    # # O(nlogm)
    # for i in range(m, n):
    #     heapq.heappushpop(heap, arr[i])
    # # O(mlogm)
    # return heap

    # 2nd approach: O(nlogn)
    # n = len(arr)
    # m = k if n > k else n
    # # O(mlogm)
    # heap = sorted(arr, reverse=True)[:m]
    # # O(mlogm)
    # heapq.heapify(heap)
    # # O(nlogm)
    # for i in range(m, n):
    #     if heap[0] < arr[i]:
    #         heapq.heapreplace(heap, arr[i])
    # # O(mlogm)
    # return heap

    # 3rd approach: O(n)
    # n = len(arr)
    # m = k if n > k else n
    # # O(mlogm)
    # heap = sorted(arr, reverse=True)[:m]
    # # O(mlogm)
    # heapq.heapify(heap)
    # # O(n)
    # for i in range(m, n):
    #     if heap[0] < arr[i]:
    #         heapq.heapreplace(heap, arr[i])
    # # O(m)
    # return heap

    # 4th approach: O(n)
    n = len(arr)
    m = k if n > k else n
    # O(m)
    heap = arr[:m]
    # O(mlogm)
    heapq.heapify(heap)
    #
