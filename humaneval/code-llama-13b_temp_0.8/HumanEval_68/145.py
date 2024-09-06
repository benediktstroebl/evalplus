
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
    def _find_min(arr):
        """
        Finds the smallest non-negative integer in a list.
        """
        min_val = None
        for val in arr:
            if min_val == None or val < min_val:
                min_val = val
        return min_val
    
    def _find_min_evens(arr):
        """
        Finds the smallest even integer in a list.
        """
        min_even = None
        for val in arr:
            if val % 2 == 0 and (min_even == None or val < min_even):
                min_even = val
        return min_even

    if len(arr) == 0:
        return []
    else:
        min_even = _find_min_evens(arr)
        if min_even == None:
            return []
        else:
            min_even_idx = arr.index(min_even)
            return [min_even, min_even_idx]

