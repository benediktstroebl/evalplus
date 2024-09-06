

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    """The sort function is used to sort the values at the indicies that are divisible by three.
    The list comprehension then takes those values, and assigns them to the corresponding indicies in the new list l',
    while leaving the indicies that are not divisible by three unchanged.
    """
    return [i if not i % 3 else sorted(l)[i // 3] for i in range(len(l))]

