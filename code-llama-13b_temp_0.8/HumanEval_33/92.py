

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # find out if list is divisible by 3
    if len(l) % 3 == 0:
        # create an empty list to store sorted items
        new_list = []
        # loop through the list, taking every 3rd item
        for i in range(0, len(l), 3):
            # loop through the list, taking every 3rd item and sort them
            for i in range(0, len(l), 3):
                new_list.append(sorted(l[i:i+3]))
            # return the list that has the sorted third items
            return new_list
    else:
        # return the original list if not divisible by 3
        return l

