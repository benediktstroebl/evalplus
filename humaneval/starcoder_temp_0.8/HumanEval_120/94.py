
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
    # A very simple approach is to use a heap of size k. Add all elements of the given array to the heap.
    # The heap will sort the largest k elements in the array.
    #
    # We can easily obtain the first k largest elements in the array by using the heapsort algorithm.
    #
    # Complexity Analysis:
    #
    # Time complexity : O(NlogK). The time complexity of the algorithm is O(NlogK)
    # where ‘N’ is the length of the array and ‘K’ is the size of the heap.
    #
    # Space complexity : O(K). The space complexity of the algorithm is O(K) as we need to
    # store ‘K’ largest elements in the heap.

    import heapq

    res = []

    # put the first k elements of the array into a min heap
    for i in range(k):
        heapq.heappush(res, arr[i])

    for i in range(k, len(arr)):
        # if the current element is smaller than the smallest element
        if arr[i] > res[0]:
            # remove the smallest element
            heapq.heappop(res)
            # and add the current element
            heapq.heappush(res, arr[i])

    # Return the elements in the heap in sorted order
    return [heapq.heappop(res) for i in range(len(res))]

