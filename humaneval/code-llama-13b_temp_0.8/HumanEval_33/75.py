

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l1 = [elem for i, elem in enumerate(l) if i % 3 != 0]
    l2 = [elem for i, elem in enumerate(l) if i % 3 == 0]
    l2 = sorted(l2)
    for i in range(0, len(l1)):
        l1.insert(2 * i + 1, l2[i])
    return l1

