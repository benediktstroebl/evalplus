
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
    # Create a heap
    heap = []
    # For each element in the array
    for num in arr:
        # If the length of heap is less than k
        if len(heap) < k:
            # Append the element to heap
            heapq.heappush(heap, num)
        else:
            # If the element is larger than the maximum element in heap
            if num > heap[0]:
                # Pop the maximum element from heap
                heapq.heappop(heap)
                # Push the element to heap
                heapq.heappush(heap, num)
    # Return the heap in descending order
    return list(reversed(heap))
