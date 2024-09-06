
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
    """
    First, we want to create a min heap of k elements. 
    We can take the first k elements from the array and create a min heap. 
    But this might not be the minimum k elements, so we have to remove elements from 
    the heap until the heap is the minimum k elements.

    We can then remove the minimum element from the heap and add a new element to the heap.
    We can do this k times and the heap will then be the minimum k elements.

    To build the heap, we can use O(n log k) where n is the number of elements in the array, 
    and k is the number of elements we want in the heap.

    We can then remove elements from the heap in O(log k) to get the minimum k elements.

    Overall, this is O(n + k log k) time complexity and O(k) space complexity.
    """
    heap = []
    for i in range(k):
        if len(heap) < k:
            heap.append(arr[i])
        else:
            if arr[i] > heap[0]:
                heap[0] = arr[i]
                heapq.heapify(heap)

    return heap

    """
    Time complexity: O(k log k + (n - k) log k) => O(n log k)
    Space complexity: O(k)
    """
    # heap = []
    # for num in arr:
    #     if len(heap) < k:
    #         heapq.heappush(heap, num)
    #     elif num > heap[0]:
    #         heapq.heapreplace(heap, num)

    # return heap

