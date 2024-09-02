

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # length of list
    x = len(l)
    # resultant list
    s = []
    # loop through the length of list
    for i in range(x):
        # if not divisible by 3
        if i % 3!= 0:
            s.append(l[i])
    # sort the elements
    s.sort()
    # put sorted elements in original list
    for i in range(x):
        if i % 3 == 0:
            l[i] = s[i // 3]
    return l
