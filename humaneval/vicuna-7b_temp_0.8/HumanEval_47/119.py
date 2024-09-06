

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # If the list is empty or has only one element, the median is that value.
    if len(l) == 0 or len(l) == 1:
        return l[0] if len(l) == 0 else l[1]
    
    # The median of a list can be found by finding the middle two elements,
    # and then calculating the average of those two elements.
    middle = len(l) // 2
    middle_index = middle - 1
    left_half = [x for x in l[len(l) // 2 - 1:middle]]
    right_half = [x for x in l[middle+1:len(l) // 2]]
    return (sum(left_half) / len(left_half), sum(right_half) / len(right_half))