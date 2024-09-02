
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
    def next_smallest(lst):
        x = lst[0]
        y = lst[1]
        for i in lst[2:]:
            if i < x:
                x = i
            if i < y and i != x:
                y = i
        return y
    return next_smallest(lst)
