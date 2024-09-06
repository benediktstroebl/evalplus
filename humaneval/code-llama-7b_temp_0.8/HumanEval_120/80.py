
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
    # # SOLUTION 1 - Quicksort
    # def quicksort(arr, low, high):
    #     if low < high:
    #         pivot_index = quicksort_partition(arr, low, high)
    #         quicksort(arr, low, pivot_index - 1)
    #         quicksort(arr, pivot_index + 1, high)

    # def quicksort_partition(arr, low, high):
    #     pivot = arr[high]
    #     i = low - 1
    #     for j in range(low, high):
    #         if arr[j] <= pivot:
    #             i += 1
    #             arr[i], arr[j] = arr[j], arr[i]
    #     arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #     return i + 1

    # # SOLUTION 2 - Sort then take top K
    # arr.sort()
    # return arr[-k:]

    # SOLUTION 3 - Heap
    import heapq

    heap = []

    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            heapq.heappushpop(heap, num)

    return heap

