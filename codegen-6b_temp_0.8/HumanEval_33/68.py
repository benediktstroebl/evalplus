

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    
    #Make a list of values that are not divisible by three - so l' would be even indices
    l_val = [n for n in l if n % 3 != 0]
    #Remaining indicies that are divisible by three are the same as the original l'
    l_indicies = [n for n in l if n % 3 == 0]

    #Sort the list using the sorted list of non-divisible values and the sorted list of divisible values
    return sorted(l_val) + sorted(l_indicies)
    
    
