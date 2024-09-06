
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


    if arr == []:
        return []

    # If array has only one node and its value is even, return it
    if len(arr) == 1:
        if arr[0] % 2 == 0:
            return [arr[0], arr[0]]
        else:
            return []

    # If array is empty, return empty list
    if arr == []:
        return []

    # Initialize smallest_value to max int, so we can keep track of the smallest even value
    smallest_value = 1000000000

    # Initialize smallest_index to -1, so we can keep track of the smallest index
    smallest_index = -1

    # Initialize even_nodes to 0, so we can keep track of the number of even nodes
    even_nodes = 0

    # Initialize odd_nodes to 0, so we can keep track of the number of odd nodes
    odd_nodes = 0

    # Iterate through the array
    for i in range(len(arr)):
        # If the current node is
