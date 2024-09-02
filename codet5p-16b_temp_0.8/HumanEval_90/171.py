
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

    min = lst[0]
    second_min = None
    for i in range(len(lst)):
        if lst[i] < min:
            second_min = min
            min = lst[i]
        elif (lst[i] < second_min) and (second_min!= None):
            second_min = lst[i]
    return second_min
