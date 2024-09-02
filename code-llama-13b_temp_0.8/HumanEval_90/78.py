
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
    
    #sort list 
    sorted_lst = sorted(lst)
    
    #return none if list is empty or there is only one element
    if len(sorted_lst) < 2:
        return None
    
    #if there are at least two elements and no dupes then return the second element 
    elif len(set(sorted_lst)) == len(sorted_lst):
        return sorted_lst[1]
    
    #if there are two of the same element return the second one 
    elif len(sorted_lst) == 3 and sorted_lst[0] == sorted_lst[1]:
        return sorted_lst[1]
    
    #if there are two of the same element and a third element return the second if it is not the same 
    elif sorted_lst[0] == sorted_lst[1] and sorted_lst[1] != sorted_lst[2]:
        return sorted_lst[2]
    
    #if there are two of the same element and a third element return the second if it is not the same 
    elif sorted_lst[1] == sorted_lst[2] and sorted_lst[0] != sorted_lst[1]:
        return sorted_lst[1]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
