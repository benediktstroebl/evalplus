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
    # Finds the index of the middle element
    mid_index = len(sorted_list) // 2
    # Check if the list has an odd number of elements, to return the middle element
    if len(sorted_list) % 2 != 0:
        return sorted_list[mid_index]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2