

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # create an empty list to store the sorted even indices
    even = []
    
    # sort the list in ascending order
    for i in range(len(l)):
        if i % 2 == 0:
            even.append(i)
        else:
            l[i] = l[i] # this will keep the original value of the odd indices
    
    # replace the values of the even indices in the list with the sorted values
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = l[even.index(i)]
    
    return l
