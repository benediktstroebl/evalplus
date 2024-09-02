

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    new_l = l
    for i in reversed(range(len(new_l)//2)):
        tmp = new_l[i]
        new_l[i] = new_l[len(new_l)-i-1]
        new_l[len(new_l)-i-1] = tmp
    return new_l
