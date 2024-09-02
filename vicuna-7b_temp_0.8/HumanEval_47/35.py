

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # sort the list
    l.sort()
    
    # check if the list is empty
    if len(l) < 2:
        return None
    
    # if the list is empty or has only one element, return that element
    if len(l) == 1:
        return l[0]
    
    # find the middle index of the list
    mid = len(l) // 2
    
    # determine if the median is the first element or the middle element
    if l[mid] <= l[mid-1] and l[mid] <= l[mid+1]:
        return l[mid]
    else:
        return (l[mid-1] + l[mid]) / 2