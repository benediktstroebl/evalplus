def pluck(arr):
    # Define the node_with_smallest_even_value variable and set it to None
    node_with_smallest_even_value = None

    # Set the smallest_even_value and smallest_index to Infinity and -1 respectively
    smallest_even_value = float('inf')
    smallest_index = -1

    # Iterate through the array
    for index, node_value in enumerate(arr):
        # Check if the current node value is even and update values if necessary
        if node_value % 2 == 0:
            if node_value < smallest_even_value:
                smallest_even_value = node_value
                smallest_index = index
            elif node_value == smallest_even_value:
                smallest_index = min(smallest_index, index)

    # Return the result
    if smallest_index == -1:
        return []
    return [arr[smallest_index], smallest_index]