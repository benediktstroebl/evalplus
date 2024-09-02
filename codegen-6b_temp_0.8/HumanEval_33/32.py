

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # l_third = [None] * len(l)
    # j = 0
    # for i in l:
    #     if i % 3 == 0:
    #         l_third[j] = i
    #         j += 1
    #     else:
    #         l_second[-j] = i
    # return l_second

    # return [i for i in l if i % 3 != 0] + [j for j in l if j % 3 == 0]
    return [i for i in l if i % 3 != 0] + [j for j in l if j % 3 == 0]
