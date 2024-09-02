
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
    if len(lst) < 2:
        return None
    else:
        smallest = lst[0]
        next_smallest = lst[0]
        for elem in lst:
            if elem < smallest:
                smallest = elem
            if elem > next_smallest and elem < smallest:
                next_smallest = elem
        return next_smallest


