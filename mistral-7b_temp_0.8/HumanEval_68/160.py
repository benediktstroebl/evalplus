
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
    # Solution 1: O(N)
    # Brute force solution, we will iterate over the array and check if the node is even and if it is smaller than the current smallest value,
    # if it is we will assign the node value to the current smallest value.
    # Time complexity: O(N)
    # Space complexity: O(1)
    # return [min(nodes), nodes.index(min(nodes))] if min(nodes) % 2 == 0 and min(nodes) != 0 else []

    # Solution 2: O(N)
    # We will create an empty list called result and set its value to None,
    # we will iterate over the array and check if the node is even and if it is smaller than the current smallest value,
    # if it is we will assign the node value to the current smallest value, and the index of the node to the current smallest index,
    # if it is the first node that is even, we will assign the node value to the current smallest value, and the index of the node to the current smallest index
    # if the smallest value is None we will assign
