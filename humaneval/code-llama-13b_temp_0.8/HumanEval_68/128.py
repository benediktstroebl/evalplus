
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
    # flag to indicate if we have found any even nodes
    found = False
    # temp array to hold index, value and flag of even node
    evens = []
    # iterate through nodes
    for index, node in enumerate(arr):
        # check if node is even
        if node%2==0:
            # if we have found at least one even node
            if found:
                # append node with its index
                evens.append([node, index])
            else:
                # flag as found
                found = True
                # append node with its index
                evens.append([node, index])
    # check if we have found any even nodes
    if found:
        # return the one with smallest value and index
        return min(evens, key=lambda x: (x[0],x[1]))
    # otherwise return empty list
    return []
