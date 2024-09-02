

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    a = l[0]
    b = l[1]
    c = l[2]
    if len(l) % 3 == 0:
        return [a, b, c]
    elif len(l) % 3 == 1:
        return [a, c, b]
    elif len(l) % 3 == 2:
        return [c, b, a]

