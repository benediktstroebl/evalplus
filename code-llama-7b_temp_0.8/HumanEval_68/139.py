
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
    #   A[2]
    # A[1] A[3]
    # A[0] A[4] A[5]
    # A[0] A[4] A[5]
    # A[0] A[4] A[5] A[6]
    # A[0] A[4] A[5] A[6]
    # A[0] A[4] A[5] A[6] A[7]
    # A[0] A[4] A[5] A[6] A[7] A[8]

    if len(arr) == 0:
        return []
    # we can find the minimum of an array in O(n) time using min_index = min(arr).
    # since we are looking for the minimum even number, we can multiply the minimum by -1 and
    # find the minimum of that, which will be the minimum even number.
    # 
    # since we know that the array will have at least one even number, the minimum of the negative 
    # array will be the minimum even number. we can then find the index of that value in the original
    # array and return the result.
    min_idx = min(range(len(arr)), key=arr.__getitem__)
    if arr[min_idx] % 2 != 0:
        return []
    return [arr[min_idx], min_idx]
