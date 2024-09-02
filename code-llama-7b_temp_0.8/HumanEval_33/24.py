

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) % 3 != 0:
        raise ValueError('Not valid input')

    l1, l2, l3 = [], [], []
    for i in range(len(l) // 3):
        l1.append(l[i])
    for i in range(len(l) // 3, 2 * len(l) // 3):
        l2.append(l[i])
    for i in range(2 * len(l) // 3, len(l)):
        l3.append(l[i])

    l1.sort()
    l2.sort()

    return l1 + l2 + l3
