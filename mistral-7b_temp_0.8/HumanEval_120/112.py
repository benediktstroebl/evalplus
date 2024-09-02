
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

    # Get a heap in which the first k elements of the list arr are inserted in sorted order.
    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])

    for j in range(k, len(arr)):
        # If arr[j] is smaller than the first element of heap, there is no need to check other elements.
        if arr[j] < heap[0]:
            continue
        # If arr[j] is greater than the first element of heap, there is no need to check other elements.
        elif arr[j] > heap[0]:
            heapq.heappush(heap, arr[j])
            heapq.heappop(heap)
    return heap

