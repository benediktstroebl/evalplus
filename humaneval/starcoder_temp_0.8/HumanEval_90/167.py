
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
    if len(lst) < 2:
        return None
    # check if the min element in the list is unique
    if lst.count(min(lst)) == 1:
        return None
    # sort the list
    lst.sort()
    # return the 2nd element
    return lst[1]
