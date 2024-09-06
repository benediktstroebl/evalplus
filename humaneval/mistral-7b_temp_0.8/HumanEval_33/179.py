

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l1 = l[:]
    new = []
    for i in range(len(l1)):
        if i % 3 == 0:
            new.append(sorted(l1[i:i+3])[0])
        else:
            new.append(l1[i])
    return new
