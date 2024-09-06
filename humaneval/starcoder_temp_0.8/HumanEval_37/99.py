

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # BEGIN SOLUTION
    even_elements = [i for i in range(0, len(l), 2)]
    odd_elements = [i for i in range(1, len(l), 2)]
    for i in even_elements:
        l[i], l[odd_elements.pop(0)] = l[odd_elements.pop(0)], l[i]
    return l
    # END SOLUTION

