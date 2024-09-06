

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # initialize a copy of the list
    sorted_list = l[:]

    # find the even indicies of the list
    even_indicies = list(filter(lambda x: x % 2 == 0, range(len(sorted_list))))

    # for each even index of the list, sort the value at that index with the values of the
    # list at the even indicies
    for index in even_indicies:
        sorted_list[index] = sorted([l[index], sorted_list[index]])[0]

    return sorted_list

