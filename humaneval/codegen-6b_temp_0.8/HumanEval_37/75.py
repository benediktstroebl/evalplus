

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    
    # Make a new list
    l2 = [None] * (len(l) // 2)

    # Insert items into l2
    for i in range(len(l2)):
        l2[i] = l[2 * i + 1]

    # Insert the remaining items of l into l2
    for item in l[len(l)//2:]:
        l2.append(item)

    # Sort l2 in-place
    l2.sort()

    # Return l2
    return l2

