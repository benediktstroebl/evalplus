def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list, [smallest_value, its index],
    If there are no even values or the given array is empty, return [].

    Examples:
        Input: [4, 2, 3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

        Input: [1, 2, 3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

        Input: []
        Output: []
    
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest even value, but there are two zeros,
                     so we will choose the first zero, wh
