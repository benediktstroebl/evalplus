

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    list_div_by_three = []
    list_not_div_by_three = []
    for i in range(len(l)):
        if i % 3 == 0:
            list_div_by_three.append(l[i])
        else:
            list_not_div_by_three.append(l[i])
    list_not_div_by_three.sort()
    list_div_by_three.sort()
    list_div_by_three.extend(list_not_div_by_three)
    return list_div_by_three

