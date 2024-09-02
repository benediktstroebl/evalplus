
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
    
    node_list = list(enumerate(arr)) # [(0, 4), (1, 2), (2, 3)]

    # sort list by value, in ascending order
    # [
    #   (2, 2),
    #   (1, 4),
    #   (0, 5)
    # ]
    node_list.sort(key=lambda node: node[1])

    # get first node with even value
    # (2, 2)
    node_even = next((node for node in node_list if node[1] % 2 == 0), None)
    if node_even is None:
        return []
    
    return [node_even[1], node_even[0]]
