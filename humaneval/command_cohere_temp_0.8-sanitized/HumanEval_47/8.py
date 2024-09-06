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
    # If the length of the list is odd, return the middle element
    if len(sorted_list) % 2 == 1:
        return sorted_list[len(sorted_list) // 2]
    # If the length is even, return the average of the two middle elements
    mid1 = len(sorted_list) // 2
    mid2 = mid1 - 1
    return (sorted_list[mid1] + sorted_list[mid2]) / 2