

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # l_even = [l[0]]
    # for i in l[1:]:
    #     if i%2 == 0:
    #         l_even.append(i)
    # l = l_even
    # l_even = []
    # for i in l:
    #     if i%2 != 0:
    #         l_even.append(i)
    # l_even = sorted(l_even)
    # l.extend(l_even)
    # return l
    l2 = []
    for i in l:
        if i%2 == 0:
            l2.append(i)
        else:
            l2.append(l[l.index(i)])
    return l2