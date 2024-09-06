def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None

    # Check if the list has only one element
    if len(l) == 1:
        return l[0]

    # Sort the list
    sorted_l = sorted(l)

    # Calculate the median
    length = len(sorted_l)
    middle_index = length // 2

    if length % 2 == 0:
        # If the number of elements is even, return the average of the two middle elements
        median = (sorted_l[middle_index - 1] + sorted_l[middle_index]) / 2
    else:
        # Otherwise, return the middle element
        median = sorted_l[middle_index]
    return median