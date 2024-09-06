
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

    # if array is empty return
    if not arr:
        return []
    
    # set smallest even value to infinity
    smallest_even_value = float('inf')
    # set smallest index to infinity
    smallest_index = float('inf')

    # iterate over list
    for index, value in enumerate(arr):
        # check if value is even and smaller than smallest value
        if (value % 2 == 0) and (value < smallest_even_value):
            # set smallest even value to current value
            smallest_even_value = value
            # set smallest index to current index
            smallest_index = index
        # check if value is even and equal to smallest value and current index is smaller than smallest index
        elif (value % 2 == 0) and (value == smallest_even_value) and (index < smallest_index):
            # set smallest index to current index
            smallest_index = index
    
    # check if smallest value is infinity
    if smallest_even_value != float('inf'):
        # return smallest even value and index in a list
        return [smallest_even_value, smallest_index]
    else:
        # return empty list
        return []
