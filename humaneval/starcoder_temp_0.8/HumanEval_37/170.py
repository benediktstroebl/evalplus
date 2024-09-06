

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    l_even = []
    l_odd = []
    l_new = []
    
    for i in l:
        if i % 2 == 0:
            l_even.append(i)
        else:
            l_odd.append(i)
    
    l_even.sort()

    for i in range(len(l)):
        if i % 2 == 0:
            l_new.append(l_even[int(i/2)])
        else:
            l_new.append(l_odd[int(i/2)])

    return l_new
