
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
    odd_values = [0 for _ in range(len(arr))]
    even_values = [0 for _ in range(len(arr))]
    index = 0
    for value in arr:
        if value % 2 == 0:
            even_values[index] = value
        else:
            odd_values[index] = value
        index += 1
    even_values.sort()
    odd_values.sort()
    if even_values and not odd_values:
        return [even_values[0], even_values[0] // 2]
    elif odd_values and not even_values:
        return [odd_values[0], odd_values[0] // 2]
    elif even_values and odd_values:
        even_value = even_values[0] if even_values[0] < odd_values[0] else odd_values[0]
        even_index = even_values.index(even_value) if even_values[0] < odd_values[0] else odd_values.index(even_value)
       
