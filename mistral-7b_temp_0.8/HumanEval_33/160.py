

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_len = len(l)
    l_list = []

    for i in range(l_len):
        if i % 3 == 0:
            l_list.append(sorted(l[i:i + 3])[0])
        else:
            l_list.append(l[i])
    return l_list

