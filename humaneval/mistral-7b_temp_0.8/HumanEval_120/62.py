
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

    if not arr or not k:
        return []

    # Create an empty list to store the sorted maximum numbers
    sorted_arr = []

    # Use a heap to keep track of the maximum k numbers
    heap = []

    # Iterate through the array
    for num in arr:
        # If the heap is empty or the current number is larger than the smallest element in the heap,
        # add the number to the heap
        if not heap or num > heap[0]:
            heapq.heappush(heap, num)

        # If the number is smaller than the smallest element in the heap,
        # remove the smallest element and add the number to the heap
        elif num < heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

        # If the heap is full, remove the smallest element and add the current number
        if len(heap) > k:
            heapq.heappop(heap)

        # Append the sorted maximum numbers to the list
        if len(heap) == k:
            sorted_
