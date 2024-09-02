

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_not_divisible_by_three = []
    l_divisible_by_three = []

    for i, item in enumerate(l):
        if i % 3 == 0:
            l_divisible_by_three.append(item)
        else:
            l_not_divisible_by_three.append(item)

    l_divisible_by_three = sorted(l_divisible_by_three)
    l_divisible_by_three_new = []

    for i, item in enumerate(l_divisible_by_three):
        l_divisible_by_three_new.append(item)

    return l_not_divisible_by_three + l_divisible_by_three_new
