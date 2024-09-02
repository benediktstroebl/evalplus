
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
    left = 0
    right = 1
    for i in range(1, len(lst)):
        if lst[i] < lst[left]:
            left = i
        elif lst[i] < lst[right]:
            right = i
        elif lst[i] == lst[right]:
            return lst[left]
    return None
