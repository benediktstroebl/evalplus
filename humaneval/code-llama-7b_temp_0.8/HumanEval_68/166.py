
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
    # A first attempt:
    #
    # In this approach, we consider the first node as the only even number
    # and iterate through the list.
    # We check each node value against our current min value.
    # If the node value is the smallest, we update it.
    # If we reach the end of the list, we return our updated min value.
    # However, this approach fails a couple of tests.
    #
    # Ex: [4,2,3]
    #
    #       (4, 0)
    #     /
    #   (2, 1)
    #
    # The correct answer should be (2, 1).
    # But this approach returns (4, 0).
    #
    # To fix this, we can keep track of the index of the node that has the
    # smallest even value.
    #
    # So our algorithm should be:
    # * Initialize the index of the node that has the smallest even value
    #   to 0.
    # * Iterate through the list.
    # * If the current node value is even and it's smaller than the min value,
    #   update the min value and the index of the min node to the current index.
    # * If we reach the end of the list, return [min_value, index_of_min_node].
    #
    # If the list is empty, we return an empty list.
    #
    # To make this approach more efficient, we can use Python's built-in
    # min function.
    #
    # As long as the list has even numbers, min will return the smallest
    # even number.
    #
    # This will also make our code more concise and readable.
    if len(arr) == 0:
        return []
    min_index = 0
    min_value = arr[0]
    for i, n in enumerate(arr):
        if n % 2 == 0 and n < min_value:
            min_index = i
            min_value = n
    return [min_value, min_index]

