

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    if len(l) == 0:
        return l

    even_indices = []
    odd_indices = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_indices.append(i)
        else:
            odd_indices.append(i)

    e = []
    o = []
    for i in even_indices:
        e.append(l[i])

    for i in odd_indices:
        o.append(l[i])

    e.sort()
    return o + e

