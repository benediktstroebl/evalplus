
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
    # 1. The easiest solution is to put all the numbers into a priority queue, 
    #    then pop the top k numbers out of it.
    # 2. However, we can do it in one pass. The idea is to use a heap to maintain 
    #    the maximum k numbers. The trick is how to compare two numbers if they 
    #    are equal.
    #
    # Hint: One way is to use their indices as a tiebreaker.
    #
    # Time complexity: O(n log k).
    # Space complexity: O(k).

    from heapq import heappush, heappop

    max_heap = []

    for index, num in enumerate(arr):
        if len(max_heap) < k:
            heappush(max_heap, (num, index))
        else:
            if num > max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (num, index))

    return [heappop(max_heap)[0] for _ in range(k)]
