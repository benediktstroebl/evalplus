

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # First, we find the size of the list
    size = len(l)
    # We set a new list that we will return
    l_even = []
    # We iterate over the original list
    for idx in range(size):
        # If the index is odd, we append it to the new list
        if idx % 2 == 1:
            l_even.append(l[idx])
        # Else, we do nothing (the index is even)
        else:
            pass
    # We sort the even indices of the original list
    l_even.sort()
    # We define another index to iterate over the original list
    idx2 = 0
    # We iterate over the new list
    for idx in range(size):
        # If the index is odd, we append the value to the new list
        if idx % 2 == 1:
            l_even.append(l[idx])
        # Else, we append the value from the sorted list
        else:
            l_even.append(l_even[idx2])
            idx2 = idx2 + 1
    # We return the new list
    return l_even

