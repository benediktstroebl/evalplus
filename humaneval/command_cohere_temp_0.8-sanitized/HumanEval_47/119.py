def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Check if the list has only one element
    if len(l) == 1:
        return l[0]
    # Sort the list
    sorted_list = sorted(l)
    # Finds the median using interpolation when there's an even number of elements
    if len(sorted_list) % 2 == 0:
        return (sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2
    # Finds the median for odd number of elements
    else:
        return sorted_list[len(sorted_list) // 2]