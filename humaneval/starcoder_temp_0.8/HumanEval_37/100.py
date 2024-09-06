

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    new_list = list(l)
    for i in range(len(new_list)):
        if i % 2 == 0:
            # set the first even index to the value of the next even index, 
            # then delete the next even index
            new_list[i] = new_list[i + 1]
            del new_list[i + 1]
    return new_list
