
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
    # min_even = min(filter(lambda x: x % 2 == 0, arr))
    # min_index = arr.index(min_even)
    # return [min_even, min_index] if min_index < min_even else []

    # better
    min_even = None
    min_index = None
    for i, el in enumerate(arr):
        if el % 2 == 0 and el != min_even:
            if (min_even is None or el < min_even) and min_index is None:
                min_even = el
                min_index = i
            elif el < min_even and min_index is not None:
                min_even = el
                min_index = i
    return [min_even, min_index] if min_index else []

