

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l2 = []
    l3 = []
    # seperate the list into two lists, one which will be sorted and one which won't
    for i in range(len(l)):
        if i % 3 == 0:
            l2.append(l[i])
        elif i % 3 == 1:
            l3.append(l[i])
        else:
            continue
    # sort the list that isn't sorted
    l2.sort()
    # zip the two lists together
    l_zipped = list(zip(l2, l3))
    # turn it back into a list
    for i in range(len(l_zipped)):
        l.append(l_zipped[i])
    return l

