
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
    # This is a greedy solution.
    # We will iterate through the array of integers and save the current index in the array
    # and the current even value.
    # If we find a new even value, we will replace the current even value and current index
    # with the new values.
    # The only exception is if the current value is even and we found a smaller value. In this case
    # we will save the new value, but we will keep the current index.
    current_even_value = -1
    current_index = -1
    for i, n in enumerate(arr):
        if n % 2 == 0:
            if current_even_value == -1 or current_even_value < n:
                current_even_value = n
                current_index = i
            elif current_even_value == n:
                current_index = min(i, current_index)
    return [current_even_value, current_index]

