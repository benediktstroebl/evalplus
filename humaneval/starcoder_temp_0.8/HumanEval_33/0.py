

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # your code here
    # third = lambda x: x % 3 == 0
    # return sorted(l, key=lambda x: (not third(x), x))
    l_three = [i for i in l if i % 3 == 0]
    l_notthree = [i for i in l if i % 3!= 0]
    return l_three + sorted(l_notthree)
