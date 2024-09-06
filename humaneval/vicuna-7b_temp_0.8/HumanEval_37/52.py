

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # calculate the length of the list
    n = len(l)
    # initialize two lists, l1 and l2
    l1 = []
    l2 = []
    # fill in the even indices of the first list with the values of the original list
    for i in range(n):
        l1.append(l[2*i])
    # fill in the even indices of the second list with the values of the original list, sorted
    for i in range(n/2):
        l2.append(sorted(l1)[i])
    # concatenate the two lists
    return l1 + l2
