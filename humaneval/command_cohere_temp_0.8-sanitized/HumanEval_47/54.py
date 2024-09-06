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
    # Finds the median in the sorted list
    # median is the middle value of the list if it has an odd number of elements
    if len(sorted_list) % 2 == 1:
        return sorted_list[len(sorted_list) // 2]
    # If the number of elements in the list is even, the median is the average of the two middle values
    middle_index1, middle_index2 = len(sorted_list) // 2, (len(sorted_list) // 2) - 1
    return (sorted_list[middle_index1] + sorted_list[middle_index2]) / 2