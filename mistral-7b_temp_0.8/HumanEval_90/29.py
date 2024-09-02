
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    i = 0
    smallest = None
    for x in lst:
        if smallest == None:
            smallest = x
        elif x < smallest:
            smallest = x
        if lst[i+1] < smallest and smallest != None:
            return lst[i+1]
        i += 1
    return None
    
