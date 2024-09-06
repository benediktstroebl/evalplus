

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = l[::-1] # sort the list in reverse order
    l = l[::3] # split the list into chunks of size 3
    l = l[::3][::-3] # sort each chunk in reverse order
    l = l[::-1][::3] # reverse each sorted chunk
    l = l[::-1] # reverse the entire list
    return l
