

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # l_2 = [l[i] for i in range(len(l)) if i % 3 == 2]
    # l_1 = [l[i] for i in range(len(l)) if i % 3 == 1]
    # l_0 = [l[i] for i in range(len(l)) if i % 3 == 0]
    # l_0 = sorted(l_0)
    # l_1 = sorted(l_1)
    # l_2 = sorted(l_2)
    # l_out = [None] * len(l)
    # for i in range(len(l)):
    #     if i % 3 == 2:
    #         l_out[i] = l_2[i // 3]
    #     elif i % 3 == 1:
    #         l_out[i] = l_1[i // 3]
    #     else:
    #         l_out[i] = l_0[i // 3]
    # return l_out
    l_out = [None] * len(l)
    for i in range(len(l)):
        if i % 3 == 2:
            l_out[i] = l[i]
        elif i % 3 == 1:
            l_out[i] = l[i]
        else:
            l_out[i] = sorted(l[i // 3])[i // 3]
    return l_out

