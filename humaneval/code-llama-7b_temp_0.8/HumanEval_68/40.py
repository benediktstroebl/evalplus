
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
    # Initial Solution
    # def pluck(arr):
    #     if len(arr) == 0:
    #         return []
    #     vals = list(filter(lambda x: x % 2 == 0, arr))
    #     if len(vals) == 0:
    #         return []
    #     index = arr.index(min(vals))
    #     return [arr[index], index]
    
    # Optimized Solution
    def pluck(arr):
        """
        :param: arr - input array
        TODO: complete this local function
        """
        # Write your code here
        min_val = arr[0]
        min_index = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] < min_val:
                min_val = arr[i]
                min_index = i
        if min_val % 2 != 0:
            return []
        return [min_val, min_index]
