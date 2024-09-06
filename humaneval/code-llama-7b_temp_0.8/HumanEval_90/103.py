
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

    # My and Best solution
    def next_smallest_my(lst):
        if len(lst) < 2:
            return None
        else:
            lst.sort()
            return lst[1]

    def next_smallest_best(lst):
        if len(lst) < 2:
            return None
        else:
            return min(lst[1:])

    return next_smallest_best(lst)
