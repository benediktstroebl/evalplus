def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    # sort the list
    l.sort()
    if n % 2 == 1:
        # if the number of elements is odd, return the middle element
        return l[n//2]
    # if the number of elements is even, return average of the two middle elements
    return (l[n//2-1] + l[n//2]) / 2