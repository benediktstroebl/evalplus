
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
    # ttungl@gmail.com
    return sorted(arr, reverse=True)[:k]
    
    
    # sol 1:
    # Heap (max heap)
    # Python: heapq.nlargest(k, arr)
    # time O(n log n)
    # space O(n)
    # runtime: 32ms
    # --
    from heapq import nlargest
    return nlargest(k, arr)
    
    
    # sol 2:
    # Heap (min heap)
    # Python: heapq.nsmallest(k, arr)
    # time O(n log n)
    # space O(k)
    # runtime: 36ms
    # --
    from heapq import nsmallest
    return nsmallest(k, arr)[::-1]
    
    
    # sol 3:
    # Heap (min heap)
    # Python: heapq.heapify(arr)
    # Python: heapq.heappop(arr)
    # time O(n log k)
    # space O(n)
    # runtime: 44ms
    # --
    import heapq
    heap = arr[:k]
    heapq.heapify(heap)
    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapq.heappushpop(heap, arr[i])
    return heap
