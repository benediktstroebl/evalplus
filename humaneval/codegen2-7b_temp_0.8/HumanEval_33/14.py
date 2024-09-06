

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l[l % 3 == 0] = 9
    l[l % 3 == 1] = 8
    l[l % 3 == 2] = 5
    l[l % 3 == 0] = 4
    l[l % 3 == 1] = 3
    l[l % 3 == 2] = 2
    l[l % 3 == 0] = 1
    l[l % 3 == 1] = 6
    l[l % 3 == 2] = 7
    l[l % 3 == 0] = 0
    
