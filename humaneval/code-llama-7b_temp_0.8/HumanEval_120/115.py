
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
    ## Time: O(Nlogk)
    ## Space: O(k)
    if len(arr) == k:
        return sorted(arr)
    k = min(k, len(arr))
    arr = sorted(arr)
    return arr[-k:]

    # heapq module for heap sort in O(Nlogk)
    # import heapq
    # n = len(arr)
    # h = [(-arr[i], i) for i in range(k)]
    # heapq.heapify(h)
    # ans = []
    # for i in range(k, n):
    #     if (-arr[i]) > h[0][0]:
    #         heapq.heappop(h)
    #         heapq.heappush(h, (-arr[i], i))
    # return sorted([-val for val, i in h])

    # minheap for sort in O(Nlogk)
    # from heapq import heappop, heappush
    # n = len(arr)
    # h = []
    # k = min(k, n)
    # for i in range(k):
    #     heappush(h, (arr[i], i))
    # ans = []
    # for i in range(k, n):
    #     if arr[i] > h[0][0]:
    #         heappop(h)
    #         heappush(h, (arr[i], i))
    # for i in range(k):
    #     ans.append(-h[i][0])
    # return ans
