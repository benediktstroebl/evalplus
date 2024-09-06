
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
    # 1) first sort the list in ascending order
    # 2) then loop through the list starting from the second index.
    #    if the current element is smaller than the one before, return the current element
    # 3) if the above loop runs without returning a value, return None
    # sort the list
    lst.sort()
    # loop through the list starting from the second index
    for i in range(1, len(lst)):
        # if the current element is smaller than the one before, return the current element
        if lst[i] < lst[i-1]:
            return lst[i]
    # if the above loop runs without returning a value, return None
    return None

