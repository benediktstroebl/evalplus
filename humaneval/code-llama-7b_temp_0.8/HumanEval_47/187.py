

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    length_l = len(sorted_l)
    # Calculate middle value of l
    if length_l % 2 == 0:
        # Even, so calculate average of middle two numbers
        # i.e. the arithmetic mean
        middle_1 = sorted_l[length_l // 2]
        middle_2 = sorted_l[length_l // 2 - 1]
        middle = (middle_1 + middle_2) / 2
    else:
        # Odd, so just pick the middle number
        middle = sorted_l[length_l // 2]
    return middle
