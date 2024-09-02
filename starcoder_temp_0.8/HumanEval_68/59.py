
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
    # get the length of the array
    n = len(arr)

    # set the minimum even value to be an arbitrarily large value
    min_even_val = 10000000

    # iterate through the array and check if any of the numbers are even
    for i, n in enumerate(arr):
        # if the number is even and the value is less than the current minimum value, update the minimum value
        if n % 2 == 0 and n < min_even_val:
            min_even_val = n
            # set the current index of the minimum even value to be i
            idx = i

    # if we found a minimum even value, return the index of that number, otherwise return None
    return [min_even_val, idx] if min_even_val!= 10000000 else None
