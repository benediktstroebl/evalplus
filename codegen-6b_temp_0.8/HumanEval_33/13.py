

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # Find the indicies that are divisible by three
    div_three = [i for i, x in enumerate(l) if x % 3 == 0]
    # Sort those indicies by the value at the corresponding indicies in l
    div_three.sort(key = l.__getitem__)
    # Use the sorted list to replace the values at the divisible indicies of l
    for i in div_three:
        l.pop(i)
        l.insert(i, l[i])
    return l

    