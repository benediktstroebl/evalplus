
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
    # Your code here
    # Return array of [value, index]
    # Empty array if there are no nodes or no even values
    # Sort the array by ascending order
    # Return the first even value and its index
    # If the first even value is at the end of the array, return the last even value and its index
    # If the first even value is the last element in the array and there are no even values, return [].
    # If there are no even values, return []


    result = []

    arr = sorted(arr)

    if arr[0]%2 == 0:
        result.append(arr[0])
        result.append(arr.index(arr[0]))

    elif arr[-1]%2 == 0:
        result.append(arr[-1])
        result.append(arr.index(arr[-1]))

    elif arr[-1]%2 != 0:
        result.append(arr[-1])
        result.append(arr.index(arr[-1]))

    return result

