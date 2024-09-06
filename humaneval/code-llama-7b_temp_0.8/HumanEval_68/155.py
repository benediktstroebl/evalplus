
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
    # store the smallest even value
    # store the index of smallest even value
    smallest_val = float("inf")
    smallest_idx = float("inf")

    # loop through the array
    for idx, num in enumerate(arr):
        # if the current number is even
        # and the current number is smaller than the smallest number
        # then update smallest_val and smallest_idx
        if num % 2 == 0 and num < smallest_val:
            smallest_val = num
            smallest_idx = idx

    # if smallest_val is equal to float("inf")
    # this means that there were no even values,
    # so we return an empty array
    if smallest_val == float("inf"):
        return []

    return [smallest_val, smallest_idx]
