from collections import *
def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes, 
    your task is to pluck one of the nodes and return it.
    
    The plucked node should be the node with the smallest even value. 
    If multiple nodes with the same smallest even value are found, 
    return the node that has the smallest index.
    
    The plucked node should be returned in a list [smalest_value, its index].
    If there are no even values or the given array is empty, return [].
    """
    # Sort the array and remove odd indices, keep -1 intact as it represents absence of a value
    arr, inv = sorted(arr), {i:i for i in range(len(arr),0,-2)}
    even = [i for i in arr if i%2 == 0]
    if even:
        return [even[0], inv[even[0]]]
    else:
        return []