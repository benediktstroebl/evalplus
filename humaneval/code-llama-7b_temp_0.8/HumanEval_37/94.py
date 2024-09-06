

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    new_list = []
    # Construct a list with the sorted even-numbered values of l
    # that is the same length as l
    for i in range(len(l)):
        if i % 2 == 0:
            new_list.append(sorted(l)[i])
        else:
            new_list.append(l[i])
    # Go through the odd indicies of l and assign them to their
    # corresponding value in new_list
    for i in range(len(l)):
        if i % 2 != 0:
            new_list[i] = l[i]
    return new_list

