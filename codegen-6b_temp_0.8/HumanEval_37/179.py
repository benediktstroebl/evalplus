

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    from math import ceil
    new_list = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            j = int(ceil((i + 1) / 2)) - 1
            new_list[j] = l[i]
            new_list[i] = l[j]
    return new_list

