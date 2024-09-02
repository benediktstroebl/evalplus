

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # ------------------------------------------------------------------
    # TODO: implement this function.
    # ------------------------------------------------------------------
    length = len(l)
    j = length
    i = 0
    even_values = []
    while i < length:
        if i % 2 == 0:
            even_values.append(l[i])
            j -= 1
        else:
            l[j] = l[i]
        i += 1
    return even_values + l[j:]



