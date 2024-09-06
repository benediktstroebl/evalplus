def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    l.sort()
    # Find the middle element
    mid = len(l) // 2
    if len(l) % 2 == 0:
        return l[mid]
    # If the list has an odd number of elements, return the middle element
    return l[mid - 1]