
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

    first_smallest = lst[0]
    second_smallest = lst[1]

    for i in range(2, len(lst)):
        if lst[i] < first_smallest:
            second_smallest = first_smallest
            first_smallest = lst[i]
        elif lst[i] < second_smallest and lst[i] > first_smallest:
            second_smallest = lst[i]

    if second_smallest == first_smallest:
        return None

    return second_smallest

