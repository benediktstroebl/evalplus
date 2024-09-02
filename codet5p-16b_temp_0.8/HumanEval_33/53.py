

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    first_index = 0
    second_index = 0
    third_index = 0
    while third_index < len(l):
        if third_index % 3 == 0:
            l[third_index] = l[first_index]
            third_index += 1
            first_index += 1
        elif third_index % 3 == 1:
            l[third_index] = l[second_index]
            third_index += 1
            second_index += 1
        else:
            third_index += 1
    return l

