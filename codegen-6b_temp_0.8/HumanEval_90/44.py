
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
    
    # Solution 1
    # Create an empty array
    # Loop over the list and append the minimum element in the new array
    # Return the 2nd smallest element of the new array
    
    if len(lst) == 0:
        return None
    else:
        new_lst = []
        for i in range(len(lst)):
            new_lst.append(min(lst))
            lst.pop(lst.index(min(lst)))
        return new_lst[1]


