

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    third_list = []
    for idx, item in enumerate(l):
        if idx % 3!= 0:
            third_list.append(item)
    third_list.sort()
    final_list = third_list + [x for idx, x in enumerate(l) if idx % 3 == 0]
    return final_list
