

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # l1 = []
    # l2 = []
    # l3 = []
    # for item in l:
    #     if item % 3 == 0:
    #         l3.append(item)
    #     elif item % 3 == 1:
    #         l2.append(item)
    #     else:
    #         l1.append(item)
    # l1.sort()
    # l2.sort()
    # l3.sort()
    # return l1 + l2 + l3
    return sorted([item for item in l if item % 3 == 0] + [item for item in l if item % 3 == 1] + [item for item in l if item % 3 == 2])

