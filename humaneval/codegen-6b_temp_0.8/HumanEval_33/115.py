

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    """Mutate l
    >>> l = [1, 2, 3, 4, 5, 6]
    >>> sort_third(l)
    [1, 2, 3, 4, 5, 6]
    """
    _not_div_by_3 = []
    _div_by_3 = []

    for num in l:
        if num % 3:
            _div_by_3.append(num)
        else:
            _not_div_by_3.append(num)

    _not_div_by_3.sort()
    _div_by_3.sort()

    new_list = []
    for i, j in zip(_not_div_by_3, _div_by_3):
        new_list.append(i)
        new_list.append(j)

    return new_list
