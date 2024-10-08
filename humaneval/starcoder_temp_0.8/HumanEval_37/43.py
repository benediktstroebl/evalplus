

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Your code here
    if len(l) == 2:
        if l[0] < l[1]:
            return l
        else:
            return l[::-1]
    elif len(l) == 0:
        return []
    else:
        return sort_even([l[0], sort_even(l[2:])])
