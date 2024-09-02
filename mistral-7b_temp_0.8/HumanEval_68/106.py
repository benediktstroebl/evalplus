
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
    # 1. Iterate through the nodes of the branch
    # 2. Find the smallest even value
    # 3. Find the node with the smallest index
    # 4. Return the node in a list [ smallest_value, smallest_index ]
    #   If there are no even values, return an empty list []

    # 1. Iterate through the nodes of the branch
    for i in range(len(arr)):
        # 2. Find the smallest even value
        if arr[i] % 2 == 0:
            # 3. Find the node with the smallest index
            min_even = arr[i]
            min_index = i
            for j in range(i, len(arr)):
                # 4. Return the node in a list [ smallest_value, smallest_index ]
                #   If there are no even values, return an empty list []
                if arr[j] % 2 == 0 and arr[j] <= min_even:
                    min_even = arr[j]
                    min_index = j
            return [min_
