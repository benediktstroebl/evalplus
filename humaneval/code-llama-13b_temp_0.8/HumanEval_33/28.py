

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    #sort the values of l that are at the indicies that are divisible by three
    index = 0
    while index < len(l):
        if index%3 != 0:
            index += 1
            continue
        l_sorted = l.copy()
        del l_sorted[index]
        l_sorted.sort()
        l[index] = l_sorted[0]
        del l_sorted[0]
        l[index+1] = l_sorted[0]
        del l_sorted[0]
        l[index+2] = l_sorted[0]
        del l_sorted[0]
        index += 3
    return l
