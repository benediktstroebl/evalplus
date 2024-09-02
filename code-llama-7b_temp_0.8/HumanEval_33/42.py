

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # this function is equivalent to doing this:
    # return l.sort(key=lambda i: i % 3)
    # but we want to use the sort function that will be introduced in the next lecture.
    # therefore, we will use the sort function from the next lecture
    l.sort(key=lambda i: i % 3)
    return l
