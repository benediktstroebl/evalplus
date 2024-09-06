

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # first extract values at indicies divisible by 3
    third_values = [l[i] for i in range(len(l)) if i % 3 == 2]
    # sort them
    third_values.sort()
    # create new list with values at indicies that are not divisible by 3 unchanged and values at indicies that are divisible by 3 replaced by values of sorted list
    l_sorted = [l[i] if i % 3 != 2 else third_values.pop(0) for i in range(len(l))]
    return l_sorted

