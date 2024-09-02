
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

    def maximum(arr, k):
        def max_heapify(arr, i):
            """
            This is a max heap operation. If a node's children's values are larger, 
            then node's value should be updated.
            """
            left = 2 * i + 1
            right = 2 * i + 2
            length = len(arr) - 1
            largest = i
            if left <= length and arr[left] > arr[i]:
                largest = left
            if right <= length and arr[right] > arr[largest]:
                largest = right

            if largest!= i:
                arr[i], arr[largest] = arr[largest], arr[i]
                max_heapify(arr, largest)
        
        def build_max_heap(arr):
            length = len(arr)
            for i in range(length // 2, -1, -1):
                max_heapify(arr, i)

        def k_largest(arr, k):
            build_max_heap(arr)
            i = len(arr) - 1
            while
