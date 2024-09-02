

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    """YOUR CODE HERE"""
    def swap_values(l, ind1, ind2):
        temp = l[ind1]
        l[ind1] = l[ind2]
        l[ind2] = temp
    new_l = l.copy()
    for i in range(len(l)):
        if i % 2 == 0:
            swap_values(new_l, i, i - 1)
    return new_l
