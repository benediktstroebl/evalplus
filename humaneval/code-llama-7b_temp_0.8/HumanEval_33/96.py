

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) == 0:
        return l
    elif len(l) == 1:
        return l
    elif len(l) == 2:
        return sorted(l)
    else:
        l1 = l[0:len(l)//3]
        l2 = l[len(l)//3:2*(len(l)//3)]
        l3 = l[2*(len(l)//3):]
        return sort_third(l1) + sort_third(l3) + sort_third(l2)

