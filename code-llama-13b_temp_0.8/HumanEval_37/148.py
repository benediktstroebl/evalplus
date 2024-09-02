

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if l == []:
        return l
    if len(l) == 1:
        return l

    i = 0
    while l[i] % 2 == 1:
        i += 1
        if i == len(l):
            break
    if i == len(l):
        return l

    j = i + 1
    while j < len(l):
        if l[j] % 2 == 1:
            i += 1
            l[i] = l[j]
            j += 1
        else:
            break

    for k in range(i + 1, len(l)):
        if l[k] < l[k - 1]:
            l[k], l[k - 1] = l[k - 1], l[k]

    return l

