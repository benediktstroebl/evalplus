

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l' = []
    even_indicies = [0, 2, 4, 6, 8]
    for i in even_indicies:
        l'.append(sorted(l)[i])
    for j in range(len(l)):
        if j not in even_indicies:
            l'.append(l[j])
    return l'

