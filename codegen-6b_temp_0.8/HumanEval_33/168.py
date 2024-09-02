

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l1 = []
    l2 = []
    l3 = []
    for count, value in enumerate(l):
        if count % 3 == 0:
            l1.append(value)
        elif count % 3 == 1:
            l2.append(value)
        else:
            l3.append(value)

    l1.sort()
    l2.sort()
    l3.sort()

    k = 0
    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = l1[k]
            k += 1
        elif i % 3 == 1:
            l[i] = l2[k - 1]
            k += 1
        else:
            l[i] = l3[k - 2]
            k += 1
    return l
