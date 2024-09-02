
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
    def compare(x,y):
        return x[0] < y[0]
    
    lst.sort(key=lambda x:x[0])
    if lst[1:]:
        return lst[1][0]
    else:
        return None
        
