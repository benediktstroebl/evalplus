

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    sorted_l = []
    for index in range(len(l)):
        if index % 3!= 0:
            sorted_l.append(l[index])
        elif index % 3 == 0:
            sorted_l.append(sorted(l[index]))
    return sorted_l
