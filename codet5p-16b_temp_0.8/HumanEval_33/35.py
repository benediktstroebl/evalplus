

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l_new = []
    l_new_third = []
    l_new_not_third = []
    for value in l:
        if l.index(value)%3 == 0:
            l_new_third.append(value)
        elif l.index(value)%3!= 0:
            l_new_not_third.append(value)
    l_new_third.sort()
    l_new_not_third.sort()
    for i in l_new_third:
        l_new.append(i)
    for i in l_new_not_third:
        l_new.append(i)
    return l_new
