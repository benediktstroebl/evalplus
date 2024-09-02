

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    n = len(l)
    mid = n // 3
    if n % 3 == 1:
        mid -= 1

    l1 = l[:mid]
    l2 = l[mid:]
    l3 = []

    while len(l1) != 0 or len(l2) != 0:
        if len(l1) != 0:
            l3.append(l1.pop())
        if len(l2) != 0:
            l3.append(l2.pop())

    return l3
