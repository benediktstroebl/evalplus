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
    middle_index = len(sorted_list) // 2
    # Check if the number of elements is odd
    if len(sorted_list) % 2 != 0:
        return sorted_list[middle_index]
    # If the number of elements is even, return the average of the two middle elements
    middle_1 = sorted_list[middle_index - 1]
    middle_2 = sorted_list[middle_index]
    return (middle_1 + middle_2) / 2