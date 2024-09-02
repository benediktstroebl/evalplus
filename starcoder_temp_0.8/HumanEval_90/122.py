
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
    n = len(lst)
    if n < 2:
        return None
    else:
        if lst[0] < lst[1]:
            minimum = lst[0]
        else:
            minimum = lst[1]
        for i in range(2,n):
            if lst[i] > minimum:
                minimum = lst[i]
                break
        return minimum
        
