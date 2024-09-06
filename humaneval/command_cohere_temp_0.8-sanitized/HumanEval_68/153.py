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
    Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Constraints:
    * 1 <= nodes.length <= 10000
    * 0 <= node.value
    """
    # Convert the list to a Set, to remove duplicate values.
    # Then convert it to a List again,
    # but this time in a sorted manner based on the even values.
    odd_values = [x for x in arr if not x % 2 == 0]
    even_values = sorted(list(set(arr)))
    if not even_values:
        return []
    elif not odd_values:
        return [min(even_values), even_values.index(min(even_values))]
    else:
        return [min(even_values), min(odd_values.index(x) for x in even_values)]