def median(l: list):
    """Return median of elements in the list l."""
    sorted_list = sorted(l)
    length = len(sorted_list)
    if length % 2 == 0:
        # If the list has an even number of elements, return the average of the two middle values
        median_ = (sorted_list[length // 2] + sorted_list[length // 2 - 1]) / 2
        return median_
    # If the list has an odd number of elements, return the middle value
    return sorted_list[length // 2]