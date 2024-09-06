
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
    # We could find the first index and ignore the rest.
    if len(lst) < 1:
        return None
    result = min(lst)
    flipped = lst[::-1]
    for i, num in enumerate(flipped):
        if num == result:
            return flipped[i + 1]
    return None

assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([]) == None
assert next_smallest([1, 1]) == None
assert next_smallest([1, 1, 1]) == None
assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
