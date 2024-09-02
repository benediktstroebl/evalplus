
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
    def is_next_smallest(lst, next_smallest):
        """
        Return True if next_smallest is the 2nd smallest element of the list.
        Return False otherwise.
        """
        if len(lst) < 2:
            return False
        if len(lst) < 3:
            return next_smallest <= lst[0]
        if lst[0] < next_smallest < lst[1]:
            return True
        else:
            return False

    return next_smallest if is_next_smallest(lst, next_smallest) else None
    
    # for every element of the list
    # check if it's the 2nd smallest
    # return the element if it is
    # return None otherwise
    
    # for element in lst:
    #     if element < lst[0] or element > lst[1]:
    #         continue
    #     return element
    # return None

