

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if not l:
        return l
    # your code here
    l1 = l[0::2]
    l2 = l[1::2]
    l2.sort()
    for i in range(len(l1)):
        l[i*2] = l1[i]
        l[i*2+1] = l2[i]
    return l
