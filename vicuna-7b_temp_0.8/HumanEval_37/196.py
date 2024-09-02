

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Check if the list is empty
    if not l:
        return []
    
    # Initialize a new list to store the sorted even indices
    l_sorted = [None] * 2
    
    # Iterate through the indices of the original list
    for i in range(0, len(l), 2):
        # Set the even index of the sorted list
        l_sorted[i] = l[i]
        
    # If the list is not empty, repeat the above steps to sort the remaining indices
    while len(l) > 0:
        # Take the first non-None element from the sorted list
        value = l_sorted[0]
        
        # If the sorted list is empty, append the next element from the original list
        if not l_sorted[1]:
            l_sorted.append(l[i])
        # If the sorted list is not empty, append the next element from the sorted list
        else:
            l_sorted.append(l_sorted[1])
            
        # Decrement the length of the original list
        l.pop(0)
            
    return l_sorted