

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # we declare a list of 0, one more than l
    l_plus = [0] * (len(l) + 1)

    for i in range(len(l)):
        # if the index is even we set the value of the value of l' at i equal to l[i]
        if i % 2 == 0:
            l_plus[i] = l[i]
        # if the index is odd we set the value of the value of l' at i equal to the value of l' at the same index - 1
        else:
            l_plus[i] = l_plus[i - 1]
    return l_plus


