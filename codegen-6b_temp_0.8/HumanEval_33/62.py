

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    less = []
    more = []
    for number in l:
        if number % 3 != 0:
            less.append(number)
        if number % 3 == 0:
            more.append(number)
    less.sort()
    more.sort()
    for i in range(len(less)):
        l[i] = less[i]
    for i in range(len(more)):
        l[i] = more[i]
    return l
