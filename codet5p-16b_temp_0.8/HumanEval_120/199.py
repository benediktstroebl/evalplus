
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

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest!= i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def build_heap(arr, n):
        for i in range(n//2, -1, -1):
            heapify(arr, n, i)

    def heap_sort(arr, n, k):
        build_heap(arr, n)
        for i in range(n-1, n-k-1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)

    return heap_sort(arr, len(arr), k)
