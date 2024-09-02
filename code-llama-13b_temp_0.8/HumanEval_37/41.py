

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    """
    neg_index = []
    pos_index = []
    pos_values = []
    neg_values = []
    for index in range(len(l)):
        if index % 2 == 0:
            neg_index.append(index)
            neg_values.append(l[index])
        elif index % 2 != 0:
            pos_index.append(index)
            pos_values.append(l[index])
    pos_values.sort()
    for index in range(len(l)):
        if index % 2 == 0:
            l[index] = neg_values[index]
        else:
            l[index] = pos_values[index]
    """
    evens = l[::2]
    evens.sort()
    l[::2] = evens
    return l



