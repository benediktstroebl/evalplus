
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
    # two passes approach
    # sort the array and take first k numbers
    # time complexity : O(nlogn)
    # space complexity: O(1)

    arr.sort()
    res = []
    for i in range(k-1, -1, -1):
        res.append(arr[i])
    return res

    # minheap approach
    # time complexity : O(nlogk)
    # space complexity: O(k)

    import heapq
    res = []
    minheap = []
    for num in arr:
        heapq.heappush(minheap, -num)
        if len(minheap) > k:
            heapq.heappop(minheap)
        res.append(-heapq.heappop(minheap))
    return res
