

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l_1 = []
    l_2 = []
    for i in range(len(l)):
        if i % 3 != 0:
            l_1.append(l[i])
        else:
            l_2.append(l[i])
    l_2.sort()
    l_1 = [l_1[i] for i in range(len(l_1))]
    l_2 = [l_2[i] for i in range(len(l_2))]
    l_1 += l_2
    return l_1

