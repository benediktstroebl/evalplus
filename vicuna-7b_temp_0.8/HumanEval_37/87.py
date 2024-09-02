

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Loop over the list
    for i in range(len(l)):
        # Compare the current element with the first element
        if i % 2 == 0:
            # If the current element is smaller than the first element, swap them
            if l[i] < l[0]:
                l[i], l[0] = l[0], l[i]
        elif i % 2 == 1:
            # If the current element is greater than the first element, swap them
            if l[i] > l[0]:
                l[i], l[0] = l[0], l[i]
    return l