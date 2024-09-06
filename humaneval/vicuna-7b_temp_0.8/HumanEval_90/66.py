
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
    # 1. If the list is empty, return None
    if not lst:
        return None
    
    # 2. If the last element of the list is the smallest element of the list, return the next smallest element
    if lst[-1] == 0:
        return lst[1]
    
    # 3. If the last element of the list is not the smallest element of the list,
    #     partition the list such that all elements less than the last element
    #     are on the left and all elements greater than or equal to the last element
    #     are on the right
    less = [x for x in lst if x < lst[-1]]
    greater = [x for x in lst if x >= lst[-1]]
    return max(less) if greater.empty? else max(less)
