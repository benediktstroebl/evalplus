

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # if the list is empty, return 0
    if len(l) == 0:
        return 0
    
    # determine the middle index of the list
    n = len(l)
    i = (n // 2) - 1
    
    # find the median by comparing the elements at the middle index with the
    # element at the index that is one index away from the middle index
    if (l[i] > l[i-1]) or (l[i] < l[i+1]):
        # if the middle element is the smallest, the median is the first
        # element
        return l[i]
    else:
        # if the middle element is the largest, the median is the last
        # element
        return l[n-1]
    
    # if the list has an odd number of elements, the median is the
    # average of the middle two elements
    # if the list has an even number of elements, the median is the
    # middle element
    if n % 2 == 1:
        return (l[i] + l[i-1]) / 2
    else:
        return l[i]
