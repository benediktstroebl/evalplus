

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # YOUR CODE HERE
    if len(l) == 0:
        return l
    index = []
    for i in range(len(l)):
        if i % 3 == 0:
            index.append(i)
    value = []
    for i in index:
        value.append(l[i])
    value.sort()
    for i in range(len(l)):
        if i in index:
            l[i] = value[index.index(i)]
    return l

