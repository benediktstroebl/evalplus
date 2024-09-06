

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    
    # Find the number of items divisible by 3
    n = 0
    for i in l:
        if i % 3 == 0:
            n += 1

    # Create a new list of the same length as l
    lnew = [0] * n

    # Loop over the indices of the items that are divisible by 3
    i = 0
    for j in range(0, n, 3):
        lnew[i] = l[j]
        lnew[i+1] = l[j+1]
        lnew[i+2] = l[j+2]
        i += 3

    return lnew

l = [1, 2, 3, 6, 5, 4, 7, 8, 9]