
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
    # -------------------------------------------------------------------------
    # PLAN
    # -------------------------------------------------------------------------
    # - Isolate odd or even?
    # - Odd values only, odd values first.
    # - Put even values in a list, 
    # - iterate through list of even values
    # - return smallest value

    # -------------------------------------------------------------------------
    # - Iterate through list and create a list of even values
    # - If a value is even, add to even list
    # - if the next value is less than the current value, remove from even list
    # - return smallest even value
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # - Iterate through list and create a list of even values
    # - if the next value is less than the current value, remove from even list
    # - return smallest even value
    # -------------------------------------------------------------------------
    from collections import deque
    # queue = deque(arr)
    smallest_val = arr[0]
    index_list = []
    # smallest_index = arr.index(smallest_val)
    # smallest_index = arr.index(arr[0])
    # return arr[0]
    smallest_even_index = 0
    for idx, value in enumerate(arr):
        if idx != len(arr) - 1:
            next_val = arr[idx + 1]
            if next_val < value:
                index_list.append(value)
            else:
                pass
        else:
            index_list.append(value)
    print(f"index_list: {index_list}")
    # return arr[0]

    if len(index_list) == 0:
        return []

    # for value in arr:
    #     if value % 2 == 0:
    #         next_value = arr.index(value)
    #         if next_value < value:
    #             index_list.append(value)
    #         else:
    #             pass
    #     else:
    #         pass

    smallest_val = min(index_list)
    smallest_even_index
