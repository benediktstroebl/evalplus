
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

    # 1.
    # heapq.nlargest(k, arr)

    # 2.
    # arr.sort()
    # return arr[-k:]

    # 3.
    # from collections import deque
    # q = deque()
    # for num in arr:
    #     if len(q) == k:
    #         if num > q[-1]:
    #             q.pop()
    #             q.append(num)
    #     else:
    #         q.append(num)
    # return list(q)

    # 4.
    from collections import deque
    q = deque()
    for num in arr:
        if len(q) == k:
            if num > q[0]:
                q.popleft()
                q.append(num)
        else:
            q.append(num)
    return list(q)
