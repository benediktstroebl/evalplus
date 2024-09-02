

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_elements = list(filter(lambda x: x % 2 == 0, l))
    even_elements.sort()
    l.sort()
    i = 0
    for j in range(0, len(l), 2):
        l[j] = even_elements[i]
        i += 1
    return l
