

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    e_indices = [i for i in range (0, len(l)) if i % 2 == 0] # indices of even elements
    e_l = [l[i] for i in e_indices] # even elements of l
    e_sorted = sorted(e_l) # sorted even elements of l
    l_l = [l[i] for i in e_indices] # even elements of l
    l_l.sort() # sort even elements of l
    for i in range(len(l_l)):
        l[e_indices[i]] = l_l[i]
    return l
