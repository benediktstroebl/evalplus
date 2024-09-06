

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # # 1-liner using the sorted built-in function
    # return sorted(l)[len(l) // 2]

    # Better 1-liner
    # return sorted(l)[len(l) // 2]

    # If the list l is empty, we return None
    if not l:
        return None

    # Make a copy of l
    lst = l[:]

    # If the list has an even number of elements, return the average of the two
    # middle elements.
    if len(l) % 2 == 0:
        # Find the two middle elements
        middle1 = len(l) // 2
        middle2 = (len(l) // 2) - 1

        # Sort the list
        lst.sort()
        # Return the average of the middle two elements
        return (lst[middle1] + lst[middle2]) / 2

    # If the list has an odd number of elements, return the middle element
    else:
        # Find the middle element
        middle = len(l) // 2

        # Sort the list
        lst.sort()
        # Return the middle element
        return lst[middle]

