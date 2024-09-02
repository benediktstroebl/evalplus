

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
    if len(l) == 0 or len(l) == 1:
        return l

    l_even = [l[i] for i in range(0,len(l)) if i % 3 == 0]
    l_odd = [l[i] for i in range(0,len(l)) if i % 3 == 1]
    l_even_sorted = sorted(l_even)

    i_odd = 0
    i_even = 0
    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = l_even_sorted[i_even]
            i_even += 1
        else:
            l[i] = l_odd[i_odd]
            i_odd += 1
    return l
