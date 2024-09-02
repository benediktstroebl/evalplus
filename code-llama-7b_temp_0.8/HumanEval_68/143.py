
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
    # Assume arr is non-empty
    # Solution 1:
    # O(n) time | O(n) space
    # ---------------------
    # The simplest solution is to iterate through all nodes and keep track of smallest even value.
    # Let's start with minimum even value and its index,
    # if current node's even value is smaller than the current minimum,
    # update minimum even value and its index.

    # return minimum_even_value, minimum_even_value_index
    minimum_even_value = float('inf')
    minimum_even_value_index = -1

    for index, node in enumerate(arr):
        if node % 2 == 0 and node < minimum_even_value:
            minimum_even_value = node
            minimum_even_value_index = index
    return [minimum_even_value, minimum_even_value_index]

    # Solution 2:
    # O(n) time | O(1) space
    # ----------------------
    # Instead of maintaining the minimum even value, we will maintain the index of minimum even value.
    # The minimum even value can change if we pluck a larger even node.
    # We can also keep track of the current minimum even value index.

    # minimum_even_value_index = -1
    # minimum_even_value = float('inf')
    # for index, node in enumerate(arr):
    #     if node % 2 == 0 and node < minimum_even_value:
    #         minimum_even_value = node
    #         minimum_even_value_index = index

    # return [minimum_even_value, minimum_even_value_index]
