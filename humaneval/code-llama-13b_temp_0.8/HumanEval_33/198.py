

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    for i in range(len(l)):
        if i%3 == 0:
            continue
        elif l[i] > l[i-1]:
            # find the index corresponding to i-1
            ind = l.index(l[i-1])
            # swap the values at l[i-1] and l[i]
            l[ind], l[i] = l[i], l[ind]
            # continue the process again
            sort_third(l)
    return l

