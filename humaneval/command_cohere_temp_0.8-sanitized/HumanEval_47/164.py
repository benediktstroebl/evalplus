def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    sorted_list = sorted(l)
    # Finds the median in case of an even number of elements
    if len(sorted_list) % 2 == 0:
        return (sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2
    # Finds the median in case of an odd number of elements
    else:
        return sorted_list[len(sorted_list) // 2]