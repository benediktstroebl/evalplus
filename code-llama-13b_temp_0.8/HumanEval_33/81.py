

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    a = []
    b = []
    c = []
    d = []
    for i in l:
        if (i % 3 == 0):
            c.append(i)
        elif (i % 3 == 1):
            b.append(i)
        else:
            a.append(i)
    for j in c:
        if (j % 3 == 0):
            d.append(j)
        elif (j % 3 == 1):
            b.append(j)
        else:
            a.append(j)
    for k in b:
        if (k % 3 == 0):
            d.append(k)
        elif (k % 3 == 1):
            b.append(k)
        else:
            a.append(k)
    for n in a:
        if (n % 3 == 0):
            d.append(n)
        elif (n % 3 == 1):
            b.append(n)
        else:
            a.append(n)
    c.sort()
    a.sort()
    b.sort()
    d.sort()
    return d+b+a
