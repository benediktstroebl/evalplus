
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
    min_index = 0
    for index in range(len(lst)):
        if lst[index] < min:
            min = lst[index]
            min_index = index
    if min_index + 1 >= len(lst):
        return None
    else:
        return lst[min_index+1]
