from collections import *
def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.

    The plucked node should be the node with the smallest even value.
    If multiple nodes with the smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list [smallest_value, its index].
    If there are no even values or the given array is empty, return [].

    Example:
    Input: [4,2,3]
    Output: [2, 1]
    Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Constraints:
    * 1 <= nodes.length <= 10000
    * 0 <= node.value
    """
    # Initialize a set to keep odd values and sort indexes
    odd_values = Set(arr)
    sorted_idx = sorted(list(enumerate(arr)), key=lambda x:[x[1],x[0]])
    
    # Filter even values and get the index of the first even value
    for idx, val in enumerate(sorted_idx):
        if val[0] % 2 == 0:
            return [val[0], idx] if len(odd_values) == 0 else [val[0], val[1]]
    
    # If no even value return empty list
    return []