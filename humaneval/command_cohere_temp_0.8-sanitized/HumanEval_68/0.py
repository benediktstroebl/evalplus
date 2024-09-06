def pluck(arr):
    """
    Pluck one node from the tree branch represented by the given array, with the constraints specified in the prompt.
    """
    # Initialize a dictionary to store nodes with their indices, initially populated with odd values, indexed by -1
    odd_indices = {}
    for i, val in enumerate(arr):
        if val % 2:
            odd_indices[val] = i
    
    # Initialize a dictionary to store even values and their indices, initially empty
    even_indices = {}
    
    # Populate the even_indices dictionary with the even values and their indices
    for i, val in enumerate(arr):
        if val % 2 == 0:
            even_indices[val] = i
    
    # If the even_indices dictionary is empty, return an empty list
    if not even_indices:
        return []

    # If there's only one even value, directly return its index
    if len(even_indices) == 1:
        return [list(even_indices.values())[0], list(even_indices.keys())[0]]

    # If there are multiple even values, sort both dictionaries by values and indices, to ensure the smallest even value is picked
    if len(even_indices) > 1:
        even_indices = {key: val for key, val in sorted(even_indices.items(), key=lambda item: [item[1], item[0]])}
        odd_indices = {key: val for key, val in sorted(odd_indices.items(), key=lambda item: [item[1], item[0]])}

    # Return the plucked node's value and index
    return [list(even_indices.values())[0], list(even_indices.keys())[0]]