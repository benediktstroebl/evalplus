
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
    import heapq
    # the heapq package allows us to easily implement a min-heap, which is ideal for this problem
    # a min-heap is a data structure that keeps track of the k smallest numbers in an array,
    # while maintaining the heap property (i.e., every parent node is smaller than its child nodes)
    # heapq.heapify(arr)
    # heapq.nlargest(k, arr)
    # heapq.nsmallest(k, arr)

    # Using heapq.nlargest(k, arr)
    return heapq.nlargest(k, arr)

