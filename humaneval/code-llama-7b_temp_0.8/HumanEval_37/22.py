

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l1 = list()
    l2 = list()
    for i in l:
        if i % 2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    l2.sort()
    j = 0
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = l2[i // 2]
        else:
            l[i] = l1[j]
            j += 1
    return l

