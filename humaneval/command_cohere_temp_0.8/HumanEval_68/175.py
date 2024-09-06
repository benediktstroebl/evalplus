Here's a Python script that solves the given problem with an efficient approach using `collections`:
```python
from collections import *

def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes, 
    your task is to pluck one of the nodes and return it.
    
    The plucked node should have the smallest even value and in case of a tie, pick the one with the smallest index.
    
    The plucked node should be returned in a list, [smalest_value, its index ], and if there are no even values or the given array is empty, return [].
    """
    # map to store the index-value dictionaries of the even values
    even_values_dict = OrderedDict()
    
    # O(n) loop to find the smallest even value and its index
    for i, val in enumerate(arr):
        if val % 2 == 0:  # if val is even
            if even_values_dict:  # if there are existing even values
                if val < list(even_values_dict.values())[0]:  # if the current val is smaller than the existing smallest even value
                    even_values_dict[i] = val  # update the dictionary
                elif val == list(even_values_dict.values())[0]:  # if the current val is equal to the existing smallest even value
                    even_values_dict[i] = val  # update the dictionary if the index of the current val is smaller
            else:
                even_values_dict[i] = val  # add the first even value to the dictionary

    # return [] if no even values are found
    if not even_values_dict:
        return []

    # return the plucked node in the required format
    return [list(even_values_dict.values())[0], list(even_values_dict.keys())[0]]
```
The approach uses `collections.OrderedDict` to efficiently store the even values and their indices for plucking. This allows for efficient comparison and selection of the node with the smallest index in case of ties. The overall time complexity of the solution is O(n), where n is the length of the input array.