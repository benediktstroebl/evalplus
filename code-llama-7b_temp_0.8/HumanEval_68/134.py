
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
    # Set the default values
    smallest_val = None
    smallest_idx = None
    smallest_idx_counter = 1

    for idx, val in enumerate(arr):
        # Find the smallest even value
        if val % 2 == 0 and smallest_val is None:
            smallest_val = val
            smallest_idx = idx
            smallest_idx_counter = 1
            continue
        # Check if the smallest even value exists
        if smallest_val is not None:
            # Find the smallest index of the smallest even value
            if val % 2 == 0 and val == smallest_val:
                if idx < smallest_idx:
                    smallest_idx = idx
                    smallest_idx_counter += 1
            # Find the smallest even value
            elif val % 2 == 0 and val < smallest_val:
                smallest_val = val
                smallest_idx = idx
                smallest_idx_counter = 1

    return [smallest_val, smallest_idx] if smallest_val else []

