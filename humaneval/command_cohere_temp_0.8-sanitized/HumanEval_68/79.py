def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes, 
    your task is to pluck one of the nodes and return it.
    
    The plucked node should have the smallest even value, and in case of a tie, 
    it should be the node that has the smallest index.
    
    The plucked node should be returned in a list [smallest_value, its index], 
    If there are no even values or the given array is empty, return [].
    
    Example:
    Input: [4,2,3]
    Output: [2, 1]

    Constraints:
    * 1 <= nodes.length <= 10000
    * 0 <= node.value
    """
    # Convert the list to a set to filter out duplicates which allows us 
    # to handle the case where there are multiple nodes with the same smallest even value
    nodes = set(arr)
    even_nodes = nodes & {x for x in nodes if x % 2 == 0}  

    return [(x, arr.index(x)) for x in even_nodes if x != smallest_even_node] or [[], 0]