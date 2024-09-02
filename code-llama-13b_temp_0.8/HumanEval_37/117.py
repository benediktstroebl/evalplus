

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # This is the list we will be building up and returning
    lp = []
    # For every index in the list,
    for i in range(len(l)):
        # if the index is even
        if i % 2 == 0:
            # add the value of the index to the result
            lp.append(l[i])
        # otherwise, the index is odd
        else:
            # add the value of the even index that comes before the current index to the result
            lp.append(l[i - 1])
    # Return the resulting list
    return lp


