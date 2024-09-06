def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    sorted_l = sorted(l)
    # Find the middle index
    middle_index = len(sorted_l) // 2
    # Check if the list has an odd or even number of elements
    if len(sorted_l) % 2 == 1:
        # If odd, return the middle element
        return sorted_l[middle_index]
    else:
        # If even, return the average of the two middle elements
        middle_element1 = sorted_l[middle_index - 1]
        middle_element2 = sorted_l[middle_index]
        return (middle_element1 + middle_element2) / 2