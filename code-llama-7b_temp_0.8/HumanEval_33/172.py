

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
    m = []
    n = []
    # This for loop makes a list of all the indicies that are divisible by three
    for i in range(len(l)):
        if i % 3 == 0:
            m.append(l[i])
        elif i % 3 == 1:
            n.append(l[i])
        else:
            pass

    # This sorts the list of values that are divisible by three
    m.sort()

    # This makes a list of the new values of the list
    p = []
    for i in range(len(l)):
        if i % 3 == 0:
            p.append(m[0])
            m.pop(0)
        elif i % 3 == 1:
            p.append(l[i])
        else:
            p.append(n.pop(0))

    return p

