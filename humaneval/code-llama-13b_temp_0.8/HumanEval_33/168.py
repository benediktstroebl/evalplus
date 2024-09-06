

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    k = len(l)
    if k==0:
        return l
    else:
        if k%3 == 2:
            a = sort_third(l[:-2])
            b = l[-2:]
            return a + b
        elif k%3 == 1:
            a = sort_third(l[:-1])
            b = l[-1:]
            return a + b
        elif k%3 == 0:
            a = sort_third(l[:-3])
            b = sorted(l[-3:])
            return a + b
