

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l_list = []
    for item in l:
        if item % 3 != 0:
            l_list.append(item)

    l_list.sort()

    l_new = []
    for item in l:
        if item % 3 == 0:
            l_new.append(l_list[int(item / 3)])
        else:
            l_new.append(item)

    return l_new

