

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    list_of_indicies = []
    for index, value in enumerate(l):
        if index % 3!= 0:
            list_of_indicies.append(index)

    sorted_list_of_indicies = sorted(list_of_indicies)
    new_list = []

    for index in sorted_list_of_indicies:
        new_list.append(l[index])

    return new_list
