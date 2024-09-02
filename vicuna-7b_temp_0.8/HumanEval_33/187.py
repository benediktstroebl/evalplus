

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # the function is the same as the previous one,
    # but it uses 3 instead of 2
    index = 0
    while index < len(l) - 1:
        if l[index] % 3 == 0:
            l[index], l[index + 1] = l[index + 1], l[index]
        index += 1
    return l
