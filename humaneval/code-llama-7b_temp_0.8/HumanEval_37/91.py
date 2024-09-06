

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # pick an even index
    i = 0
    l_even = []
    l_odd = []
    # run through each element in l
    while i < len(l):
        # if the index is even, add it to the even list
        if i % 2 == 0:
            l_even.append(l[i])
        # if the index is odd, add it to the odd list
        else:
            l_odd.append(l[i])
        i += 1
    # now sort the even list
    l_even.sort()
    # create a new list
    l_new = []
    # now add the sorted even list and the odd list, alternating
    for i in range(len(l_even)):
        l_new.append(l_even[i])
        l_new.append(l_odd[i])
    return l_new

