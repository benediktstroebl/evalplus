
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
    if len(arr) == 0:
        return []

    # To avoid mutating the input array, we create a copy
    arr = arr.copy()

    # This will be used to store the smallest node's value and index
    smallest_node = [float('inf'), -1]

    # This will be used to store the smallest node with even value
    # which has the smallest index
    smallest_node_with_even_value = [float('inf'), -1]

    for index, node in enumerate(arr):
        if node % 2 == 0:
            smallest_node_with_even_value = min(
                smallest_node_with_even_value, [node, index])

        smallest_node = min(smallest_node, [node, index])

    if smallest_node_with_even_value[0] <= smallest_node[0]:
        return smallest_node_with_even_value

    return smallest_node
