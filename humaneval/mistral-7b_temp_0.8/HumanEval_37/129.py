

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l2 = []
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            even_index = l.index(l[i], even_index)
        l2.append(l[i])
    l2[even_index:even_index + 2] = sorted(l2[even_index:even_index + 2])
    return l2

