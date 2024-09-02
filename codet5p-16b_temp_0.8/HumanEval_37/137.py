

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    even = []
    odd = []
    final = []
    for item in l:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    even.sort()
    odd.sort()
    for i in range(len(even)):
        final.append(even[i])
        final.append(odd[i])
    return final
    
