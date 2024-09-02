

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    # Empty list
    if not l:
        return l

    # list with only 1 element
    if len(l) == 1:
        return l

    # list with at least 2 elements
    else:
        l1 = []
        l2 = []
        l3 = []
        l4 = []

        for i in l:
            if i % 3 == 0:
                l4.append(i)
            elif i % 3 == 1:
                l1.append(i)
            elif i % 3 == 2:
                l2.append(i)
            else:
                print("error")

        l1.sort()
        l2.sort()
        l3.sort()
        l4.sort()

        l.clear()

        for i in l1:
            l.append(i)
        for i in l2:
            l.append(i)
        for i in l3:
            l.append(i)
        for i in l4:
            l.append(i)

        return l

    #    i = 0
    #    l.sort()
    #    while i < len(l):
    #        if i % 3 == 0:
    #            l.pop(i)
    #            l.insert(i, l[i - 1])
    #            l.pop(i - 1)
    #            i = i - 1
    #        i = i + 1
    #
    #    return l
    #
    #    l_sorted = []
    #    l_new = []
    #    for i in l:
    #        if i % 3 == 0:
    #            l_sorted.append(i)
    #        else:
    #            l_new.append(i)
    #
    #    l_new.sort()
    #
    #    for i in l_new:
    #        l.append(i)
    #    for i in l_sorted:
    #        l.append(i)
    #
    #   
