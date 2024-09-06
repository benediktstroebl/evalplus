
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
    # find the min of even values
    # return [min, min_index] if min != None else []

    # even_vals = list(filter(lambda x: x % 2 == 0, arr))
    # print(f"even vals: {even_vals}")
    # if len(even_vals) > 0:
    #     return [min(even_vals), even_vals.index(min(even_vals))]
    # return []
    
    # loop through arr
    # if any even value is found, keep track of its index
    # if no even values are found, return []
    # once even value is found, return [even_value, even_value_index]
    # O(n) time | O(1) space

    # min_even_val = None
    # min_even_val_index = None

    # for idx, val in enumerate(arr):
    #     if val % 2 == 0:
    #         if min_even_val == None:
    #             min_even_val = val
    #             min_even_val_index = idx
    #         else:
    #             if val < min_even_val:
    #                 min_even_val = val
    #                 min_even_val_index = idx

    # if min_even_val != None:
    #     return [min_even_val, min_even_val_index]
    # return []

    # one line
    # O(n) time | O(1) space
    return [min([val, idx] if val % 2 == 0 else None for idx, val in enumerate(arr)), min([idx for idx, val in enumerate(arr) if val % 2 == 0])] if any(val % 2 == 0 for val in arr) else []

