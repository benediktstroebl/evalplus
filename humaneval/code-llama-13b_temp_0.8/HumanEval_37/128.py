

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if len(l) == 1:
        return l

    if len(l) == 2:
        if l[1] > l[0]:
            return l[::-1]
        else:
            return l

    if len(l) % 2 != 0:
        raise ValueError

    split = len(l) // 2
    even_sorted = sort_even(l[split:])
    even_sorted.extend(l[:split])

    return even_sorted

