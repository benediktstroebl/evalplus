def pluck(arr):
    if not arr:
        return []

    # Filter even values and get their index
    even_values = [i for i, val in enumerate(arr) if val % 2 == 0]
    
    if not even_values:
        return []

    # Get the minimum even value and its index
    min_val, min_index = min(even_values), even_values[0]

    # Check if there are multiple occurrences of the minimum even value
    if len(even_values) > 1:
        # Filter the occurrences of the minimum even value and get the index of the minimum index
        min_index = min(even_values[1:], key=lambda x: x[1])[1]

    return [min_val, min_index]