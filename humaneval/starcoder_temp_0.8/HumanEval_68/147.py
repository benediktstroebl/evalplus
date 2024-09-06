
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
    # this is a hash map to store the index of even values and their actual values
    even_map = {}
    # this will store the final plucked index and value
    plucked_even = []
    # this will be used for the second value in the list
    smallest_index = 0
    # this will be used to check if we can find even values in the array
    even_values_found = False

    # loop through the array
    for i, node in enumerate(arr):
        # check if the current node is even
        if node % 2 == 0:
            # add it to the hash map
            even_map[node] = i
            even_values_found = True
        # if the node is odd, check if we found even values in the array
        elif even_values_found:
            # get the current minimum even value in the hash map
            min_even = min(even_map.keys())
            # if the current node is less than the minimum, update the minimum value
            if node < min_even:
                min_even = node
                smallest_index = i
            # update the value in the hash map
            even_map[min_even] = i
    
    # check if we found even values
    if even_values_found:
        # return the plucked even value
        plucked_even.append(min_even)
        # return the plucked value's index
        plucked_even.append(even_map[min_even])
    # else return an empty array
    else:
        plucked_even = []

    # return the final list
    return plucked_even
