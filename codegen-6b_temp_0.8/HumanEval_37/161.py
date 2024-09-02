

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if type(l) != list:
        return l
    else:
        length = len(l)
        if length == 0 or length == 1:
            return l
        else:
            l[0:length:2] = sorted(l[0:length:2])
            return l

