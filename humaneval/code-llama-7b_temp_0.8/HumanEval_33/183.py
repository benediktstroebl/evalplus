

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    # empty list case
    if l == []:
        return []

    # length 1 list case
    if len(l) == 1:
        return l

    # if length of list is divisible by three, recurse over first two thirds and append third
    if len(l) % 3 == 0:
        return sort_third(l[:len(l) // 3]) + l[len(l) // 3:2 * len(l) // 3] + sort_third(l[2 * len(l) // 3:])

    # if length of list is not divisible by three, recurse over first two thirds and append third
    else:
        return sort_third(l[:len(l) // 3 + 1]) + l[len(l) // 3 + 1:2 * len(l) // 3] + sort_third(l[2 * len(l) // 3:])

