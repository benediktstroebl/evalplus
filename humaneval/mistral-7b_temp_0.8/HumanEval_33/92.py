

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    new_list = []
    for i in l:
        if i % 3 == 0:
            new_list.append(sorted(l[i:i + 3]))
            new_list[-1] = new_list[-1][0]
        else:
            new_list.append(l[i])
    return new_list
