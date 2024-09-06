
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
    
    # Sort the list
    lst.sort()
    
    # Check if there's a second smallest element
    if len(lst) >= 2:
        return lst[1]
    else:
        return None

assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([]) == None
assert next_smallest([1, 1]) == None
assert next_smallest([-1, -2, -3]) == -2
assert next_smallest([2, 1, 3, 4, 5]) == 2
assert next_smallest([5, 2, 3, 1, 4]) == 2
assert next_smallest([2, 2, 3, 4, 5]) == None
assert next_smallest([5, 8, 3, 1, 4]) == 3
assert next_smallest([5, 5, 3, 1, 4]) == None
assert next_smallest([5, 5, 3, 2, 4]) == 3

