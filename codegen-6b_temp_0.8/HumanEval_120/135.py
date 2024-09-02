
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
    def _init_heap(arr):
        n = len(arr)
        for i in range(n, -1, -1):
            max_heapify(arr, i)
        return arr

    def max_heapify(arr, i):
        max_index = i
        left, right = i * 2 + 1, i * 2 + 2
        if left < len(arr) and arr[left] > arr[max_index]:
            max_index = left
        if right < len(arr) and arr[right] > arr[max_index]:
            max_index = right
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
            max_heapify(arr, max_index)
            
    arr = _init_heap(arr)
    result = []
    for i in range(k):
        result.append(arr[0])
        arr[0] = arr[-1]
        arr.pop()
        max_heapify(arr, 0)
    return result

