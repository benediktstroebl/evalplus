
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
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return None
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[1]
        else:
            return None
    else:
        lst.sort()
        for i in range(len(lst)-2):
            if lst[i] < lst[i+1] < lst[i+2]:
                return lst[i+1]
    return None


