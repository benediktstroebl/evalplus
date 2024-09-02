

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    i = 0
    while i < len(l):
        if i % 3 == 0:
            z = l[i]
            y = l[i + 1]
            x = l[i + 2]
            if x < y:
                if x < z:
                    if y < z:
                        l[i] = x
                        l[i + 1] = y
                        l[i + 2] = z
                    else:
                        l[i] = x
                        l[i + 1] = z
                        l[i + 2] = y
                else:
                    l[i] = z
                    l[i + 1] = x
                    l[i + 2] = y
            else:
                if y < z:
                    l[i] = y
                    l[i + 1] = z
                    l[i + 2] = x
                else:
                    if x < z:
                        l[i] = y
                        l[i + 1] = x
                        l[i + 2] = z
                    else:
                        l[i] = y
                        l[i + 1] = x
                        l[i + 2] = z
            i = i + 3
        else:
            i = i + 1
    return l
