def pluck(arr):
    """
    Plucks and returns the smallest even value from the tree branch array,
    or returns [] if no even values or the array is empty.
    Prioritizes the node with the smallest index in case of ties.
    """
    even_nodes = [node for node in arr if node % 2 == 0]
    if not even_nodes or not arr:
        return []

    smallest_even = min(even_nodes)
    smallest_index = min([i for i, node in enumerate(arr) if node == smallest_even])

    return [smallest_even, smallest_index]