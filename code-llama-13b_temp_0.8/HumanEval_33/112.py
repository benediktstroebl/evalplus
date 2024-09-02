

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l_copy = l.copy()
    sorted_list = sorted(l_copy)
    counter = 0
    for i in range(0, len(l)):
        if i % 3 == 0:
            sorted_list[i] = l[counter]
            counter = counter + 1

    return sorted_list
