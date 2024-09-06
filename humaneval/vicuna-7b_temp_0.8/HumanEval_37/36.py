

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    n = len(l)
    # A list to store the even sorted values
    even_vals = [x for x in l]
    # Iterating over the even indices
    for i in range(n//2):
        # Swapping values with the next element
        even_vals[i], even_vals[i+1] = even_vals[i+1], even_vals[i]
    return [x for x in even_vals]