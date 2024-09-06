

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    temp_list = []
    new_list = []
    for i in l:
        if l.index(i)%3 == 0:
            temp_list.append(i)
        else:
            new_list.append(i)
    new_list.sort()
    return new_list + temp_list

