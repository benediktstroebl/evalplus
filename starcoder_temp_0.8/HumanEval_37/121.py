

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    n = len(l)
    if n == 0 or n == 1:
        return l
    elif n == 2:
        if l[0] > l[1]:
            return [l[1], l[0]]
        else:
            return l
    else:
        return (l[0::2] + sort_even(l[1::2]))
