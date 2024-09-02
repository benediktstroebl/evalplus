

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_div_3 = [x for x in range(len(l)) if x % 3 == 0]
    l_mod_3 = [x for x in range(len(l)) if x % 3 != 0]
    l_sorted = sorted(l[i] for i in l_div_3)
    l_final = []
    for i in range(len(l)):
        if i in l_mod_3:
            l_final.append(l[i])
        else:
            l_final.append(l_sorted[l_div_3.index(i)])
    return l_final

