
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
    smallest = min(lst)
    smallest_pos = lst.index(smallest)
    second_smallest = None
    for pos in range(smallest_pos+1, len(lst)):
        if lst[pos] < smallest:
            smallest = lst[pos]
            second_smallest = smallest
    if second_smallest == None:
        for pos in range(0, smallest_pos):
            if lst[pos] < smallest:
                smallest = lst[pos]
                second_smallest = smallest
    return second_smallest
