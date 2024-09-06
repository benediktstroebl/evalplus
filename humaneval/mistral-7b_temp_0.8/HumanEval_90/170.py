
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
    for i in range(len(lst)):
        if lst[i-1]>lst[i]:
            return lst[i]
    else:
        return None
    # def next_smallest(lst):
    #     if len(lst) == 0:
    #         return None
    #     smallest = min(lst)
    #     for i in range(len(lst)):
    #         if lst[i] == smallest:
    #             return lst[i]
    #     else:
    #         return None
    # # next_smallest([1, 2, 3, 4, 5])
    # # next_smallest([5, 1, 4, 3, 2])
    # # next_smallest([])
    # # next_smallest([1, 1])

