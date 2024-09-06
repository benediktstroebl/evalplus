

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    third_index = int(len(l) / 3)
    l1 = l[:third_index]
    l2 = l[third_index:]
    l1.sort()
    l2.sort()
    for i in range(third_index):
        if l1[i] < l2[i]:
            l1[i], l2[i] = l2[i], l1[i]
    l[:third_index] = l1
    l[third_index:second_index] = l2
    return l
