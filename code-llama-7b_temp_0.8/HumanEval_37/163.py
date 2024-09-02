

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # solve in linear time
    return sorted(l, key=lambda x: x % 2 == 0)

    # solve in quadratic time
    # list_even = []
    # list_odd = []
    # for i in range(len(l)):
    #     if i % 2 == 0:
    #         list_even.append(l[i])
    #     else:
    #         list_odd.append(l[i])
    # list_even.sort()
    # list_output = []
    # for i in range(len(l)):
    #     if i % 2 == 0:
    #         list_output.append(list_even.pop(0))
    #     else:
    #         list_output.append(list_odd.pop(0))
    # return list_output

