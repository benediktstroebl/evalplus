

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    even_indices = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_indices.append(i)
    l_even = []
    for i in even_indices:
        l_even.append(l[i])
    l_even.sort()
    final_l = []
    for i in range(len(l)):
        if i % 2 == 0:
            final_l.append(l_even[0])
            l_even.pop(0)
        else:
            final_l.append(l[i])
    return final_l

