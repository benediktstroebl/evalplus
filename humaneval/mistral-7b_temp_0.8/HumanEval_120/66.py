
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
    if not arr:
        return []

    def heapify(arr, start, end):
        """
        Given an array arr and a positive integer k, return a sorted list of length k with the maximum k numbers in arr.

        Example:

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3

        Output: [9, 8, 7]
        """
        # Get the largest value in the array
        largest = start
        for i in range(start + 1, end):
            if arr[i] > arr[largest]:
                largest = i

        # Swap the largest value with the first value
        arr[start], arr[largest] = arr[largest], arr[start]

        # Recursively heapify the subarray from the start to the end
        heapify(arr, start + 1, end)

    def build_max_heap(arr, start, end):
        """
        Given an array arr and
