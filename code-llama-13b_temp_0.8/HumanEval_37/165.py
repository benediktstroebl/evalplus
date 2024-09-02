

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    for i in range(0, len(l), 2):
        even_number = l[i]
        small = even_number
        j = i + 1
        while j < len(l):
            if l[j] < small:
                small = l[j]
            j += 2
        l[i] = small
        j = i + 1
        while j < len(l):
            if l[j] < even_number and l[j] != small:
                even_number = l[j]
            j += 2
        l[i + 1] = even_number
    return l

