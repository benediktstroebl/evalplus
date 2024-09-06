
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
    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) > 1:
        small_lst = [i for i in lst if i < lst[0]]
        return small_lst[1] if len(small_lst) > 1 else None

lst = [3, 4, 2, 1]
