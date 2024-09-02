
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
    # sort the list
    l = sorted(lst)
    # if the list is empty
    if len(l) == 0:
        return None
    # if there is only one element in the list
    elif len(l) == 1:
        return None
    # if the first element of the list is the smallest
    elif l[0] < l[1]:
        return l[1]
    # if the last element is the smallest
    elif l[-1] < l[-2]:
        return l[-1]
    # return the second smallest
    else:
        return l[1]
