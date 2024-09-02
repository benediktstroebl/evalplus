

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    
    for i in range(1,len(l),2):
        # get the index of the even value
        even_index = l[i]
        # if our index is even, swap the value with the value at the even index
        # and move on to the next index
        if i % 2 == 0:
            l[i] = l[i-1]
        # otherwise, swap the values at the even index with the value at the
        # even index in the even list
        else:
            l[i] = even_index
    
    return l
