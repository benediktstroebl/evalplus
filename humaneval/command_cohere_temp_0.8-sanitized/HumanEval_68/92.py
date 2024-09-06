def pluck(arr):
    # Identify even values and their indices in the list
    even_values = [idx for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_values:
        return []

    # Determine the index of the smallest even value
    smallest_even_index = min(even_values, key=even_values.count)

    # Verify if there are multiple nodes with the same smallest even value
    if len(even_values) > 1:
        # Sort the even values based on their indices
        even_values.sort()
        # Ensure the plucked node has the smallest index among equal values
        return [arr[smallest_even_index], smallest_even_index]
    
    # If there's only one node with the smallest even value, return it
    return [arr[smallest_even_index], smallest_even_index]