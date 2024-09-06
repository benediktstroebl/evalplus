
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
    """
    Need to keep track of the even values, and return the smallest one.
    Then, we need to keep track of the indexes of the even values.
    To determine which index is the smallest, we need to compare the indexes.
    The complexity of this algorithm is O(n), where n is the length of the array.
    We need to iterate through the array once to find the smallest even value and its index.
    """
    if len(arr) == 0:
        return []
    even_vals = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_vals.append(arr[i])
            even_vals.append(i)
    smallest_even_val = min(even_vals[0:len(even_vals):2])
    smallest_even_index = even_vals[0:len(even_vals):2].index(smallest_even_val)
    return [smallest_even_val, smallest_even_index]

