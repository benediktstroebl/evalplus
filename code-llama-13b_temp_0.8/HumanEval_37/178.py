

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    assert type(l) == list
    if l == []:
        return []
    if len(l) == 1:
        return l

    sorted_even_list = sort_even(l[2:])
    sorted_even_list.insert(0, l[1])
    sorted_even_list.insert(0, l[0])
    return sorted_even_list


