

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # new_list = []
    # for i in l:
    #     if i % 3 == 0:
    #         new_list.append(i)
    #     else:
    #         new_list.append(i)
    #
    # new_list.sort()
    #
    # return new_list

    # list_copy = l[:]
    # for i in range(len(list_copy)):
    #     if i % 3 == 0:
    #         list_copy[i] = l[i]
    #     else:
    #         list_copy[i] = l[i]
    #
    # list_copy.sort()
    #
    # return list_copy

    return sorted(l, key=lambda x: (x % 3,x))
