
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
    def dfs(arr, i):
        if i == len(arr) - 1:
            return [arr[i], i]
        for j in range(i, len(arr)):
            if arr[j] % 2 == 0:
                dfs(arr, j)
    
    smallest_index = 0
    smallest_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] % 2 == 0:
            dfs(arr, i)
            if smallest_value > arr[i]:
                smallest_value = arr[i]
                smallest_index = i
    
    return smallest_value, smallest_index