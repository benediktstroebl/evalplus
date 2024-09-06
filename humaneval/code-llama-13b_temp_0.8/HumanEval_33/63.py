

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # start with an empty list
    new_list = []
    # iterate over the list while taking 3 indicies at a time
    for i in range(0, len(l), 3):
        # make a slice
        sublist = l[i:i+3]
        # if there are only 1 or 2 indicies left, just add them directly
        if len(sublist) <= 2:
            new_list += sublist
        # otherwise, sort the sublist and append it to the new list
        else:
            new_list += sorted(sublist)
    # return the new list
    return new_list

