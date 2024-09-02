

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    sorted_third_list = [None] * len(l)
    index = 0
    while index < len(l):
        if index % 3 == 0:
            sorted_third_list[index] = sorted(l[index: index + 3])
            index = index + 3
        else:
            sorted_third_list[index] = l[index]
            index = index + 1
    return sorted_third_list
