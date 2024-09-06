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

    # Finds the median in odd counts
    if len(sorted_list) % 2 == 1:
        return sorted_list[len(sorted_list) // 2]

    # If the count is even, return average of two middle elements
    middle1 = sorted_list[len(sorted_list) // 2 - 1]
    middle2 = sorted_list[len(sorted_list) // 2]
    return (middle1 + middle2) / 2