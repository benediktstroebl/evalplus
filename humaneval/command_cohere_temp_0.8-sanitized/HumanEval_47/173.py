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
    # Find the median using the following logic:
    # If the length of the list is odd, the median is the middle element
    if len(sorted_list) % 2 == 1:
        return sorted_list[len(sorted_list) // 2]
    # If the length is even, the median is the average of the two middle elements
    middle_index1 = len(sorted_list) // 2 - 1
    middle_index2 = len(sorted_list) // 2
    return (sorted_list[middle_index1] + sorted_list[middle_index2]) / 2