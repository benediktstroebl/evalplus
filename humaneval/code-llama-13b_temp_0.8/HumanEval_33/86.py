

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    third_l = []
    for i in range(len(l)):
        if i % 3 == 0:
            third_l.append(l[i])
    for i in range(len(l)):
        if i % 3 != 0:
            third_l.append(l[i])
    third_l.sort()
    return third_l
