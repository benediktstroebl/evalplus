

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l1 = l[:]
    for i in range(0, len(l1), 3):
        if i % 3 == 0:
            sub_list = l[i:i + 3]
            sub_list.sort()
            l[i] = sub_list[0]
            l[i + 1] = sub_list[1]
            l[i + 2] = sub_list[2]
    return l1

