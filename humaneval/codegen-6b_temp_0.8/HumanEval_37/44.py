

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if len(l) < 3:
        return l

    # Break l into a groups of odd and even indicies
    odds = [l[i] for i in range(1, len(l), 2)]
    evens = [l[i] for i in range(0, len(l), 2)]
    
    # Sort the odd items
    odds.sort()
    
    # Insert the sorted evens at their correct location
    for i in range(len(evens)):
        odds.insert(i*2, evens[i])
    
    return odds


