
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
    def heapify(unsorted, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and unsorted[i] < unsorted[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and unsorted[largest] < unsorted[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            unsorted[i], unsorted[largest] = unsorted[largest], unsorted[i]  # swap

            # Heapify the root.
            heapify(unsorted, n, largest)

    # The main function to sort an array of given size
    def heap_sort(unsorted, n):
        # Build a maxheap.
        for i in range(n // 2 - 1, -1, -1):
            heapify(unsorted, n, i)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            unsorted[i], unsorted[0] = unsorted[0], unsorted[i]  # swap
            heapify(unsorted, i, 0)

    # The main function to extract k maximum numbers from given array
    def get_k_max(arr, k):
        heap_sort(arr, len(arr))
        return arr[-k:]

    return get_k_max(arr, k)

