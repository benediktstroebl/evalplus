

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l_third = []
    l_temp = []
    for i in l:
        if (l.index(i) % 3) == 0:
            l_third.append(i)
        else:
            l_temp.append(i)
    l_temp.sort()
    l_third.extend(l_temp)
    return l_third
