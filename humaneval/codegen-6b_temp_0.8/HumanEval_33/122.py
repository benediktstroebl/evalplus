

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    #We want sorted_l to be a copy of l, without the indicies divisible by 3, while the values at those indicies are the same as the values of the corresponding indicie in l
    sorted_l = l[:]
    for i in range(0, len(l), 3):
        if i == len(l) - 1:
            sorted_l[i] = l[i]
        else:
            sorted_l[i] = l[i]
            sorted_l[i] = l[i+1]

    return sorted_l

