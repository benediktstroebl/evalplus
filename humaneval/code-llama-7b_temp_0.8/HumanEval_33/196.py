

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    result = []
    for i in range(0, len(l), 3):
        result.append(l[i])
    result.sort()
    result2 = []
    for i in range(0, len(l), 3):
        result2.append(l[i])
    for i in range(0, len(result)):
        result2[i] = result[i]
    return result2

