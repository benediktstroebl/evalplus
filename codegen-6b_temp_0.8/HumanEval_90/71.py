
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
    sorted_lst = sorted(lst)
    sorted_lst.reverse()
    try:
        idx = lst.index(sorted_lst[0])
        if idx + 1 < len(lst):
            return sorted_lst[idx + 1]
    except ValueError:
        return None
    