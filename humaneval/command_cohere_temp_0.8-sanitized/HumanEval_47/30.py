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
    # Find the middle element
    middle = len(sorted_l) // 2
    if len(sorted_l) % 2 == 0:
        return sorted_l[middle]
    # If the number of elements is odd, return the middle element
    return sorted_l[middle - 1]