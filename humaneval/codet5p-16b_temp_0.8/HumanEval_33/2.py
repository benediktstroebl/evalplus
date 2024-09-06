

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    new_l = [None]*len(l)
    divisible = []
    ind = 0
    while ind < len(l):
        if ind % 3 == 0:
            divisible.append(l[ind])
        else:
            new_l[ind] = l[ind]
        ind += 1
    divisible.sort()
    for ind, val in enumerate(new_l):
        if val is None:
            new_l[ind] = divisible.pop()
    return new_l
