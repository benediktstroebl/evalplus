

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # Hint: First figure out how to sort a list.
    # Hint: Make a helper function that takes in a sublist l' and returns a sorted sublist of l'.
    # Hint: Make a helper function that takes in an int n and returns the indicies of the list l that are divisible by n.
    # Hint: Use the helper function on indicies 0 and 1 and check that the resulting list is identical to the original.
    # Hint: Use the helper function on index 2 and check that the resulting list is sorted.
    return sorted(l)



