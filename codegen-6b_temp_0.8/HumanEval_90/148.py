
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
    if len(lst) < 2:
        return None
    else:
        min_lst = [min(lst[0], lst[1])]
        if lst[0] < lst[1]:
            lst.remove(lst[0])
        for i in lst[1:]:
            if i < min_lst[0]:
                min_lst = [i]
            elif i < min_lst[0] and i not in min_lst:
                min_lst.append(i)
        return min_lst[1]
