
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

    # init
    even_arr = []
    max_val = 0
    min_val = 9999
    min_index = 9999

    # in-place solution
    for index, val in enumerate(arr):
        # store only even values
        if val % 2 == 0 and val > max_val:
            even_arr = []
            even_arr.append(val)
            max_val = val
            min_val = max_val
            min_index = index
        # store only even values and if value is less then current min
        elif val % 2 == 0 and val < max_val:
            even_arr.append(val)
            max_val = val

    # return list of min even value and min even value index
    if even_arr:
        return [even_arr[0], min_index]

    return []

