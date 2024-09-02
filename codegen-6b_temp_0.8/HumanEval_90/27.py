
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
    if len(lst) == 0:
        return None

    smallest = None
    for el in lst:
        if smallest is None or el < smallest:
            smallest = el

    if smallest is not None:
        return sorted(lst)[1]
    else:
        return None

assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([]) is None
assert next_smallest([1, 1]) is None
assert next_smallest([1,2,3,4,5]) is None
assert next_smallest([-1,-2]) is None
assert next_smallest([-1,-2,0]) == 0
assert next_smallest([-1,-2,0,1,2]) == 0
assert next_smallest([-2,-1,0]) == 0
assert next_smallest([-2,-1,0,1,2]) == 0
assert next_smallest([-2,-1,0,1,2,5]) == 5

next_smallest([1,2,3,4,5])
next_smallest([5,1,4,3,2])
next_smallest([])
next_smallest([1,1])
next_smallest([1,2,3,4,5])
next_smallest([-1,-2])
next_smallest([-1,-2,0])
next_smallest([-1,-2,0,1,2])
next_smallest([-2,-1,0])
next_smallest([-2,-1,0,1,2])
next_smallest([-2,-1,0,1,2,5])
