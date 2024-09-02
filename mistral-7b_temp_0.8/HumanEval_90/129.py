
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
    smallest_one = lst[0]
    smallest_two = lst[0]
    for i in lst:
        if smallest_one > i:
            smallest_one = i
        if smallest_two > i:
            smallest_two = i
        if smallest_two == i:
            smallest_two = lst[lst.index(i)+1]
    if smallest_one == smallest_two:
        return None
    else:
        return smallest_two

