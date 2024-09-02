

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # We then use a for loop to iterate through the list, and for each index, we
    # create a new list of the even indices which are sorted, with the elements of
    # the odd indices as we go.
    odd_list = []
    for index in range(len(l)):
        if index % 2 != 0:
            odd_list.append(l[index])
        else:
            odd_list.append(sorted(l[index])[-1])
    return odd_list
