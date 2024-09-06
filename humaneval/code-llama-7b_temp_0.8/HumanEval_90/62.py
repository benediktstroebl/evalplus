
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

    # if len(lst) < 2:
    #     return None
    # if lst[1] < lst[0]:
    #     return lst[1]
    # for i in range(1, len(lst)):
    #     if lst[i] < lst[i - 1]:
    #         return lst[i]
    # return None
    if lst == None:
        return None
    else:
        first = lst[0]
        for i in range(len(lst)):
            if lst[i] < first:
                first = lst[i]

        for i in range(len(lst)):
            if lst[i] > first:
                return lst[i]
    return None

