
def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    # import sys
    # sys.setrecursionlimit(100000)
    # def deep_recurse(arr, i):
    #     if len(arr) == 0:
    #         return [], 0, [], 0
    #     elif len(arr) == 1:
    #         return [arr[0]], 1, [], 1
    #     else:
    #         if int(arr[0]) % 2 == 0:
    #             m = deep_recurse(arr[1:], i)
    #             if m[0][0] % 2 == 0 and m[1] < i:
    #                 return m
    #             elif m[0][0] % 2 != 0:
    #                 return deep_recurse(arr[1:], i + 1)
    #         else:
    #             m = deep_recurse(arr[1:], i)
    #             if m[0][0] % 2 != 0 and m[1] < i:
    #                 return m
    #             elif m[0][0] % 2 != 0:
    #                 return deep_recurse(arr[1:], i + 1)

    # # print(deep_recurse([1,2,3, 4, 5], 0))
    # m = deep_recurse(arr, 0)
    # return m

    if len(arr) == 0:
        return []
    idx, min_idx = None, None
    min_idx, min_val = 0, None
    for i, v in enumerate(arr):
        if v % 2 == 0:
            if min_idx is None:
                min_idx = i
                min_val = v
            if v < min_val:
                min_idx = i
                min_val = v
        # print(f"{i} {v} {min_idx}")
    if min_idx is None:
        return []
    return [min_val, min_idx]

