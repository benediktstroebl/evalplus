

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # list_copy = l[:]
    #
    # even_numbers = [x for x in list_copy if x % 2 == 0]
    # even_numbers.sort()
    #
    # i = 0
    # while i < len(list_copy):
    #     if list_copy[i] % 2 == 0:
    #         list_copy[i] = even_numbers.pop(0)
    #     i += 1
    # return list_copy

    even_list = []
    odd_list = []
    for x in l:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)
    even_list.sort()
    even_list.extend(odd_list)
    return even_list

