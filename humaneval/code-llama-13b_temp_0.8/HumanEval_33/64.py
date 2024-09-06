

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l_aux = [a for a in l]
    third_list = []
    for a in l:
        if a % 3 == 0:
            third_list.append(a)
            l_aux.remove(a)
    sorted_list = sorted(third_list)

    for i in range(len(l)):
        if i % 3 == 0 and i < len(sorted_list):
            l[i] = sorted_list[i // 3]
        else:
            l[i] = l_aux[i // 3]
            l_aux.remove(l[i])

    return l

