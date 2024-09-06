

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # we define l'
    new_list = [0] * len(l)

    # loop over l' and set the values of l' at odd indicies to the values of l at the corresponding indicies
    for i in range(len(l)):
        if i % 2 != 0:
            new_list[i] = l[i]

    # loop over l and set the values of l' at even indicies to the values of l at the corresponding indicies
    for i in range(len(l)):
        if i % 2 == 0:
            new_list[i] = l[i]

    # sort the values of l' at even indicies
    new_list.sort()

    return new_list

