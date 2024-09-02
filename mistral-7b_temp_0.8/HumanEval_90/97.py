
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
    lst_2 = []
    for num in lst:
        if num not in lst_2:
            lst_2.append(num)
    lst_2.sort()
    if len(lst_2) < 2:
        return None
    else:
        return lst_2[1]

