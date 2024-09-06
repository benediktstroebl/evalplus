

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Your code here
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    new_list = list(range(0, len(evens)))
    for i in new_list:
        l[i * 2] = evens[i]
        l[i * 2 + 1] = odds[i]
    return l

