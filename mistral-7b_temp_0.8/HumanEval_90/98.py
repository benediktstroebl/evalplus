
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
    s = [1, 1]
    if lst == []:
        return None
    if lst[0] == lst[1]:
        return None
    else:
        if lst[0] < lst[1]:
            s.append(lst[0])
            s.append(lst[1])
        else:
            s.append(lst[1])
            s.append(lst[0])
        lst = s
    return lst[0]
