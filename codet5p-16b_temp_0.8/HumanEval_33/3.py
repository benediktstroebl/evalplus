

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    a = [0, 0]
    b = [0, 0]
    c = [0, 0]
    for i in range(len(l)):
        if i % 3 == 0:
            a[1] = l[i]
        elif i % 3 == 1:
            b[1] = l[i]
        else:
            c[1] = l[i]
    a[0] = sorted(a)
    b[0] = sorted(b)
    c[0] = sorted(c)
    a[1] = sorted(a[1])
    b[1] = sorted(b[1])
    c[1] = sorted(c[1])
    a[1] = a[1][1]
    b[1] = b[1][1]
    c[1] = c[1][1]
    a = a[0] + a[1]
    b = b[0] + b[1]
    c = c[0] + c[1]
    return a + b + c

