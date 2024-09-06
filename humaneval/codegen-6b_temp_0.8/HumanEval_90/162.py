
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
    if not lst:
        return None
    
    min1 = lst[0]
    min2 = None
    for i in range(1, len(lst)):
        if min2 is None or lst[i] < min2:
            min2 = lst[i]
    return min2

assert(next_smallest([1, 2, 3, 4, 5]) == 2)
assert(next_smallest([5, 1, 4, 3, 2]) == 2)
assert(next_smallest([]) == None)
assert(next_smallest([1, 1]) == None)
