

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    
    # your code here
    
    third = int(len(l)/3)
    l2 = l[:third]
    l3 = l[third:]
    
    l2.sort()
    l3.sort()
    
    for i in range(len(l)-1):
        if (i/3)%3 == 0:
            l[i] = l2[i/3]
        else:
            l[i] = l3[i - (i/3)*3]
    
    return l
    
    