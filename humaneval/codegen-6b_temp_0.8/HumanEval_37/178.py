

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    "*** YOUR CODE HERE ***"
    l1 = []
    l2 = []
    l3 = []
    for i in l:
        if i % 2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    while l1:
        l3.append(l1.pop())
    while l2:
        l3.append(l2.pop())
    return l3
