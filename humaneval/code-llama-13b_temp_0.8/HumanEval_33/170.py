

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    list_sort = [i for i in l if l.index(i) % 3 != 0]
    list_sort.sort()
    list_sort_third = []
    for i in range(len(l)):
        if l.index(l[i]) % 3 == 0:
            list_sort_third.append(list_sort[0])
            list_sort.remove(list_sort[0])
        else:
            list_sort_third.append(l[i])
    return list_sort_third

