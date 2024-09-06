

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Use the median of 22 as the pivot, and partition the list into
    # the lower half and the upper half.
    l = l[::2] # use the generator expression to slice the list in O(1) time
    pivot = l[0]
    lower_half = [x for x in l if x < pivot]
    upper_half = [x for x in l if x >= pivot]
    # Count the number of elements in each half.
    lower_half_count = len(lower_half)
    upper_half_count = len(upper_half)
    # If the upper half has more elements, the median is the mean of the two
    # largest elements in the upper half.
    if upper_half_count > lower_half_count:
        return sum(upper_half[i] for i in range(upper_half_count)) / (upper_half_count - 1)
    # Otherwise, the median is the mean of the two largest elements in the
    # lower half.
    else:
        return sum(lower_half[i] for i in range(lower_half_count)) / (lower_half_count - 1)
