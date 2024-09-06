
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
    # O(n log n)
    lst.sort()
    if len(lst) >= 2:
        return lst[1]
    return None

    # O(n)
    # for i, x in enumerate(lst):
    #     if i > 0 and x < lst[i - 1]:
    #         return x
    # return None
