
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
    if len(lst) == 1:
        return None
    if len(lst) == 2:
        return min(lst)
    if lst[0] > lst[1]:
        return lst[1]
    if lst[-1] > lst[-2]:
        return lst[-2]
    return min(lst[:2])

assert(next_smallest([1, 2, 3, 4, 5]) == 2)
assert(next_smallest([5, 1, 4, 3, 2]) == 2)
assert(next_smallest([]) == None)
assert(next_smallest([1, 1]) == None)
assert(next_smallest([1, 2, 3]) != 2)
assert(next_smallest([1,2,1]) == 2)