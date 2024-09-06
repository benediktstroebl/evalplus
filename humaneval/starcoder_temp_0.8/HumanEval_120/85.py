
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
    # # Sorting
    # arr.sort()
    # return arr[-k:]

    # # Heap
    # heap = arr[:k]
    # heapq.heapify(heap)
    # for num in arr[k:]:
    #     heapq.heappushpop(heap, num)
    # return heap

    # # Priority Queue
    # queue = []
    # for num in arr:
    #     heapq.heappush(queue, -num)
    # return [-heapq.heappop(queue) for _ in range(k)]

    # Two Pointers
    ans = []
    start, end = 0, k - 1
    while end < len(arr):
        if arr[end] > arr[start]:
            ans.append(arr[end])
            end += 1
        else:
            ans.append(arr[start])
            start += 1
    if start == end:
        ans.append(arr[start])
    return ans + arr[start+1:]
