
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

    # Set the smallest_value to 0
    smallest_value = 0

    # Set the smallest_index to 0
    smallest_index = 0

    # Loop through each value in the array
    for i, value in enumerate(arr):
        # If the value is even and the smallest_value is 0, or
        # If the value is even and the smallest_value is greater than the value
        if value % 2 == 0 and (smallest_value == 0 or value < smallest_value):
            # Set the smallest_value to the current value
            smallest_value = value
            # Set the smallest_index to the current index
            smallest_index = i

    # If there are no even values, return an empty list
    if smallest_value == 0:
        return []
    # Else, return a list containing the smallest_value and smallest_index
    return [smallest_value, smallest_index]
