def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.

    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list [smallest even value, its index].
    If there are no even values or the given array is empty, return [].

    Example:
    Input: [4,2,3]
    Output: [2, 1]

    Constraints:
    * 1 <= nodes.length <= 10000
    * 0 <= node.value
    """
    # Your code here!
    if not arr:
        return []

    # Sort the array based on even values followed by index
    even_indices = [i for i, n in enumerate(arr) if n % 2 == 0]
    arr = [el for el in arr if el % 2 == 0 or el not in even_indices] + even_indices

    return [min(arr), arr.index(min(arr))]