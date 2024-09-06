

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # for i in range(1, len(l)):
    #     if i % 2 == 0:
    #         even_number = l[i]
    #         for j in range(i + 1, len(l)):
    #             if l[j] < even_number:
    #                 l[j], l[i] = l[i], l[j]
    # return l
    return ([element for index, element in sorted(
        [(i, element) for (i, element) in enumerate(l) if i % 2 == 1], key=lambda x: x[1])] +
            [element for index, element in sorted(
                [(i, element) for (i, element) in enumerate(l) if i % 2 == 0], key=lambda x: x[1])])

