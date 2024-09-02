

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l1 = []
    for i in range(0, len(l), 2):
        l1.append(l[i])
    l2 = []
    for i in range(1, len(l), 2):
        l2.append(l[i])
    l2 = sorted(l2)
    l3 = []
    for i in l2:
        l3.append(i)
    l4 = []
    for i in l3:
        l4.append(i)
    l5 = []
    for i in range(0, len(l), 2):
        l5.append(l4[i])
    l6 = []
    for i in range(1, len(l), 2):
        l6.append(l5[i])
    l6 = l6 + l5
    return l6

