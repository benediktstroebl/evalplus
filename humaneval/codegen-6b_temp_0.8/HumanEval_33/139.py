

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # l' = []
    # for i in range (len(l)):
    #     if i % 3 != 0:
    #         l' = l' + [l[i]]
    # sorted_l = sorted(l[i])
    # l' = l' + sorted_l
    # return l'
    # if i % 3 != 0:
    #     l' = l' + [i]
    # sorted_l = [l[i]]
    # for j in range (i + 1, len(l)):
    #     if j % 3 != 0:
    #         sorted_l += [l[j]]
    # l' = sorted(l) + sorted_l
    # return l'
    return l[0::3] + [i for i in sorted(l[1::3])] + l[2::3]

