

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    if len(l) == 2:
        if l[0] % 3 == 0:
            return [l[0], l[1]]
        elif l[1] % 3 == 0:
            return [l[1], l[0]]
        else:
            return l
    l_copy = []
    for i in range(0, len(l), 3):
        l_copy.append(sorted(l[i: i + 3]))
    result = []
    for i in range(0, len(l_copy)):
        result += l_copy[i]
    return result
