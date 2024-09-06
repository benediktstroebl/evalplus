def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    sorted_list = sorted(l)
    # Finds the middle index
    middle_index = len(sorted_list) // 2
    if len(sorted_list) % 2 == 0:
        # If the list has an even number of elements, return the average of the two middle elements
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        # If the list has an odd number of elements, return the middle element
        median = sorted_list[middle_index]
    return median