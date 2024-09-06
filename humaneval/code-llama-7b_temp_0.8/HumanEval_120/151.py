
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
    if k == 0:
        return []

    # The idea is to use a heap to keep the top k items.
    # To make the heap faster, we use the array as a max-heap.
    # See: https://en.wikipedia.org/wiki/Heapsort
    #
    # How does it work?
    # - To get the top k items, we first build a max-heap using the first k elements.
    # - Then we update the heap using the remaining elements.
    # - To get the result, we pop the elements from the heap.
    #
    # Complexity:
    #   - Time O(n log k)
    #   - Space O(k)

    def _max_heapify(arr, heap_size, i):
        l = i * 2 + 1
        r = i * 2 + 2
        largest = i

        if l < heap_size and arr[largest] < arr[l]:
            largest = l
        if r < heap_size and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            _max_heapify(arr, heap_size, largest)

    def _update_heap(arr, heap_size, start, end):
        for i in range(start, end + 1):
            _max_heapify(arr, heap_size, i)

    def _get_result(arr, heap_size):
        res = []
        for i in range(k):
            res.append(arr[0])
            _max_heapify(arr, heap_size, 0)
        return res

    # Convert the list to array
    arr = list(arr)

    # The heap size is initially k.
    heap_size = k

    # Build a max-heap with the first k elements.
    _max_heapify(arr, heap_size, 0)

    # Update the heap with the remaining elements.
    _update_heap(arr, heap_size
