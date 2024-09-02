

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    temp = []
    for i in l:
        if (i % 3 == 0):
            temp.append(i)
    temp.sort()
    for i in range(0, len(l)):
        if (l[i] % 3 == 0):
            l[i] = temp[0]
            temp.pop(0)

    return l




