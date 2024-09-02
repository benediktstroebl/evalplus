

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    index = 1
    while index < len(l):
        if index % 3 == 0:
            pass
        else:
            third_index = index - index % 3
            third_value = l[third_index]
            current_value = l[index]
            if current_value > third_value:
                temp = l[index]
                l[index] = l[third_index]
                l[third_index] = temp
                index = third_index
            else:
                index += 1
    return l

