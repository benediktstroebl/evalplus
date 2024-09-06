

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    third_i = 0
    while third_i < len(l) - 1:
        i = third_i + 1
        while i < len(l) - 1 and l[i] % 3 == 0:
            i += 1
        if third_i!= i:
            l[third_i], l[i] = l[i], l[third_i]
        third_i += 1
    return
