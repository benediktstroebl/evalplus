
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
    res = []
    if k == 1:
        return [max(arr)]
    elif k == len(arr):
        return sorted(arr)
    elif len(arr) < k:
        return sorted(arr)
    else:
        # for i in range(k):
        #     res.append(max(arr))
        #     arr.remove(max(arr))
        # return res
        # res = arr[:k]
        # heapq.heapify(res)
        # for i in range(k, len(arr)):
        #     if res[0] < arr[i]:
        #         heapq.heapreplace(res, arr[i])
        # return res
        for i in range(k):
            res.append(max(arr))
            arr.remove(max(arr))
        return res

