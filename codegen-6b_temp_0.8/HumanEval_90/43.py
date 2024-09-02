
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
    n = len(lst)
    assert n > 0
    assert n == len(set(lst))
    if n == 1:
        return None
    if n == 2:
        i = lst.index(min(lst))
        return lst[i+1]
    answer = min(lst)
    lst.remove(answer)
    return next_smallest(lst)
    
assert next_smallest([1, 3]) == 3
assert next_smallest([1, 2, 1]) == 2
assert next_smallest([1, 3, 2]) == 3
assert next_smallest([1, 3, 4, 2]) == 2
assert next_smallest([4, 3, 2, 1]) == 2
assert next_smallest([]) is None
assert next_smallest([1, 1]) is None
