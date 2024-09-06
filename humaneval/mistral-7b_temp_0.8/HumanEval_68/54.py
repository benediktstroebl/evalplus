
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
    # Initialize the result list and even counter
    result = []
    even_count = 0

    # Iterate over each node in the array
    for i, node in enumerate(arr):
        # If the node is even, increment the even counter
        if node % 2 == 0:
            even_count += 1
        else:
            # If the node is odd, check if there are any even nodes
            if even_count == 0:
                # If there are no even nodes, set the result to empty list
                result = []
            else:
                # If there are even nodes, set the result to the smallest even node and its index
                result = [arr[even_count - 1], even_count - 1]
                # Break the loop
                break
    return result

