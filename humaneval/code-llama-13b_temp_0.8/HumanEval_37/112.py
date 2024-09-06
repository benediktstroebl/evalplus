

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # remove the odd indicies of l
    l1 = list()
    for i in range(len(l)):
        if i % 2 == 1:
            l1.append(l[i])
    # sort l1
    l1.sort()
    # merge the two lists in the required order
    l2 = list()
    l3 = list()
    for i in range(len(l)):
        if i % 2 == 0:
            l2.append(l[i])
        else:
            l3.append(l1[int(i / 2)])
    return l2 + l3

