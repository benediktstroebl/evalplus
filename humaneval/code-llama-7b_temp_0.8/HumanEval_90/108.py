
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
    
    # If the list contains less than 2 elements, return None
    if len(lst) < 2:
        return None
    
    # Create a new list of length 1 with the first element of the original list
    new_lst = lst[0:1]
    
    # Iterate through all elements of the original list
    for element in lst:
        # If the first element is smaller than the last element of the new list, we found the next smaller element
        if element < new_lst[-1]:
            return element
        # If not, append the element to the new list
        else:
            new_lst.append(element)
    
    # If we reach here, the list contains only 1 element
    return None
    
    
    
