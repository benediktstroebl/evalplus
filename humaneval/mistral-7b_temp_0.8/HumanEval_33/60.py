

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = [i for i in l if i % 3 == 0]
    l = sorted(l)
    l_1 = l[0]
    l_2 = l[1]
    l_3 = l[2]
    l = [i for i in l if i % 3 == 1]
    l = [i for i in l if i % 3 == 2]
    l = [i for i in l if i % 3 != 0]
    l = [l_1] + l + [l_2] + l + [l_3]
    return l

