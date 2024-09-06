

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    odd_indicies = []
    even_indicies = []
    for index in range(len(l)):
        if index % 2 == 0:
            even_indicies.append(index)
        else:
            odd_indicies.append(index)
    odd_indicies.sort()
    even_indicies.sort()
    sorted_even = []
    for even_index in even_indicies:
        sorted_even.append(l[even_index])
    sorted_odd = []
    for odd_index in odd_indicies:
        sorted_odd.append(l[odd_index])
    l[:] = sorted_odd + sorted_even
    return l
