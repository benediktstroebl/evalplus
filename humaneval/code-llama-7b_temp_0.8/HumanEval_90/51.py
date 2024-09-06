
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
    # Your code here
    # for i in range(len(lst)):
    #     lst_sorted = sorted(lst)
    #     lst_sorted.remove(lst_sorted[0])
    #     return lst_sorted[0]
    return sorted(lst)[1] if sorted(lst)[1:] else None

