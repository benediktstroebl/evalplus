
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
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            min_lst = lst[i]
            min_lst_idx = i
    if lst[min_lst_idx] < lst[min_lst_idx+1]:
        min_lst = lst[min_lst_idx+1]
        min_lst_idx = min_lst_idx+1
    return min_lst
