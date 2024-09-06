
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
    if len(lst) == 0:
        return None
    else:
        first = lst[0]
        second = lst[1]
        smallest = second
        for i in range(2, len(lst)):
            if lst[i] <= first and lst[i] < smallest:
                smallest = lst[i]
            elif lst[i] < first and lst[i] >= smallest:
                first = lst[i]
        return smallest
