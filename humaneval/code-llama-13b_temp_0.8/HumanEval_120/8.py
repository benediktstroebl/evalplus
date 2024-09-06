
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

    def heapify(arr, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2
        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child
        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child
        if largest != root_index:
            arr[root_index], arr[largest] = arr[largest], arr[root_index]
            heapify(arr, heap_size, largest)

    n = len(arr)
    if k > n: return arr
    heap = arr[:k]
    heap_size = k
    for i in range(k // 2 - 1, -1, -1):
        heapify(heap, heap_size, i)
    # print(heap)
    for i in range(k, n):
        if heap[0] < arr[i]:
            heap[0] = arr[i]
            heapify(heap, heap_size, 0)
    return heap

