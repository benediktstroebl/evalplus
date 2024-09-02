
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
    # To do this in linear time, you need to do this in two passes
    # First pass check for the smallest even value, and find it's index
    # Second pass check for the smallest index of all the even values,
    # if the same even value is found twice, check the smaller index.
    # 
    # Keep a running smallest_even_value
    # Keep a running smallest_even_value_index
    # Keep a running current_index
    # Loop over all items in arr:
    #    if the current item is even and less than smallest_even_value
    #       set smallest_even_value to current item
    #       set smallest_even_value_index to current_index
    #    if the current item is even and equal to smallest_even_value
    #       check if smallest_even_value_index is greater than current_index
    #       if so set smallest_even_value_index to current_index
    #    increment current_index
    # return a list of [ smallest_even_value, smallest_even_value_index ]
    smallest_even_value = 0
    smallest_even_value_index = 0
    current_index = 0
    for i in arr:
        if i % 2 == 0 and i < smallest_even_value:
            smallest_even_value = i
            smallest_even_value_index = current_index
        elif i % 2 == 0 and i == smallest_even_value:
            if current_index < smallest_even_value_index:
                smallest_even_value_index = current_index
        current_index += 1
    if smallest_even_value:
        return [smallest_even_value, smallest_even_value_index]
    return []
