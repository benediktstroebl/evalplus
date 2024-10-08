

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
    list_len = len(l)
    for i in range(0, list_len, 2):
        if i + 1 < list_len:
            new_list.append(min(l[i], l[i + 1]))
            new_list.append(max(l[i], l[i + 1]))
        else:
            new_list.append(l[i])
    return new_list

