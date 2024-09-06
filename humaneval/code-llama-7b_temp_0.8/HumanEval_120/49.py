
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
    # Sorting algorithm
    # O(knlog(k)) time, O(n) space

    arr.sort()
    return arr[len(arr)-k:]

    # Heap
    # O(knlog(k)) time, O(k) space

    heap = []
    for i in range(k):
        if i == 0:
            heapq.heappush(heap, arr[i])
        else:
            heapq.heappush(heap, arr[i] - heap[0])
    
    return [heapq.heappop(heap)+heap[0] for i in range(k)]

    # Quick select
    # O(n) time, O(n) space

    if k == 1:
        return [max(arr)]

    pivot = arr[0]
    left, right = [], []
    for i in range(len(arr)):
        if arr[i] >= pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])
    
    left = maximum(left, k-1)
    right = maximum(right, k-1)
    return [pivot] + left + right

    # Median of Medians
    # O((n + k)log(k)) time, O(k) space

    def kth_smallest_median_of_medians(arr, k):
        medians = []
        for i in range(0, len(arr), 5):
            medians.append(median(arr[i:i+5]))
        
        return kth_smallest(medians, k)

    def median(arr):
        arr.sort()
        return arr[len(arr) // 2]

    def kth_smallest(arr, k):
        pivot = kth_smallest_median_of_medians(arr, len(arr) // 2 + 1)
        left, right = [], []
        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
           
