
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

    def _smallest(lst):
        """
        Helper function to get smallest element from list.
        """
        smallest = None
        for num in lst:
            if smallest is None:
                smallest = num
            elif num < smallest:
                smallest = num
        return smallest

    lst.remove(_smallest(lst))
    return _smallest(lst)
