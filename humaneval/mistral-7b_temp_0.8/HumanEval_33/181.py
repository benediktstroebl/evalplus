

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    # Your code goes here
    # These are the values that are not divisible by three
    not_divisible = [i for i in range(len(l)) if i % 3 != 0]
    # Here we are forming the l' by replacing the values at the indices that are divisible by three
    # with sorted values of the corresponding indices of l
    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = sorted(l)[i//3]
    return l
