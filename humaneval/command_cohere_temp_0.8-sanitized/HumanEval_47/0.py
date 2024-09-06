def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    sorted_l = sorted(l)
    # Find the middle index
    middle_index = len(sorted_l) // 2
    # Check if the list has an odd number of elements
    if len(sorted_l) % 2 != 0:
        # The median is the middle element
        return sorted_l[middle_index]
    # If the list has an even number of elements, return the average of the two middle elements
    return (sorted_l[middle_index - 1] + sorted_l[middle_index]) / 2