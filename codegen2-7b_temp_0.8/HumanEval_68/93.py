
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
    def pluck(arr, start, end):
        if start == end:
            return arr[start], start
        
        if start > end:
            return []
        
        mid = (start + end) // 2
        smalest, smalest_index = pluck(arr, start, mid)
        biggest, biggest_index = pluck(arr, mid + 1, end)
        
        if smalest % 2 == 0 and biggest % 2 == 1:
            return smalest, smalest_index
        elif smalest % 2 == 1 and biggest % 2 == 0:
            return biggest, biggest_index

        return smalest if smalest > biggest else biggest, biggest_index
    
    return pluck(arr, 0,
