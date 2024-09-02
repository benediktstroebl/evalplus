

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
        return []
    else:
        l1 = l[:]
        l2 = l[:]
        idx = 0
        for i in range(len(l)):
            if i % 3 == 0:
                l2.sort()
                idx = 0
            else:
                l1[i] = l2[idx]
                idx += 1
        return l1

