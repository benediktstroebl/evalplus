

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # hint: use l[::3] to get the values at the indicies that are not divisible by three
    # hint: use sorted(l[::3]) to get the values at the indicies that are not divisible by three, but sorted
    # hint: use l[::-3] to get the values at the indicies that are divisible by three
    # hint: use zip(l[::-3], sorted(l[::3])) to combine the indicies that are divisible by three with the indicies that are not divisible by three
    # hint: use list(zip(l[::-3], sorted(l[::3]))) to convert the combined lists into a list
    # hint: use list(zip(l[::-3], sorted(l[::3])))[0] to get the combined lists without the last value
    return None
