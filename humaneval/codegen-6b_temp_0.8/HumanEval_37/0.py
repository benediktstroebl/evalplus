

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    index = 0
    while index < len(l) - 1:
        if l[index] % 2 == 0 and l[index + 1] % 2 == 0:
            index += 1
        elif l[index] % 2 == 0 and l[index + 1] % 2 != 0:
            smallest = min(l[index], l[index + 1])
            l.remove(smallest)
            l.insert(0, smallest)
            index += 1
        else:
            index += 1
    return l
