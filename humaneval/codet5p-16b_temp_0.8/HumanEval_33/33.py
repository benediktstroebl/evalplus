

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    indexes_divisible_by_three = []
    indexes_not_divisible_by_three = []
    for i in range(len(l)):
        if i % 3 == 0:
            indexes_divisible_by_three.append(i)
        else:
            indexes_not_divisible_by_three.append(i)
    list_third_list = sorted(l)
    for i in indexes_divisible_by_three:
        list_third_list[i] = l[i]
    return list_third_list
