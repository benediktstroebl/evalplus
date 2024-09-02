

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # your code here
    n = len(l)
    m = n % 3
    if m != 0:
        l = l[:n - m]
    l1 = [x for i, x in enumerate(l) if i % 3 == 0]
    l2 = [x for i, x in enumerate(l) if i % 3 == 1]
    l3 = [x for i, x in enumerate(l) if i % 3 == 2]
    l1.sort()
    l2.sort()
    l3.sort()
    return [i + j + k for i, j, k in zip(l1, l2, l3)]
