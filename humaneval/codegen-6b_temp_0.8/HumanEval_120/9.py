
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
    def __maximum_k(arr, k):
        if k == 0 or k > len(arr):
            return []

        max_k_min_heap = MinHeap()
        for index in range(len(arr)):
            if len(max_k_min_heap) == k:
                max_k_min_heap.pop()
            max_k_min_heap.push(arr[index])

        result = [0] * k
        for index in range(k):
            result[index] = max_k_min_heap.peek()
            max_k_min_heap.pop()
        return result

    shuffle(arr)
    return __maximum_k(arr, k)

