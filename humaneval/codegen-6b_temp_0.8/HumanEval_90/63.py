
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
    if len(lst) < 2:
        return None

    min_index = None

    for i in xrange(len(lst) - 1):
        if lst[i] < lst[-1]:
            if min_index is None or lst[i] > lst[min_index]:
                min_index = i
        else:
            if min_index is None or lst[-1] < lst[min_index]:
                min_index = len(lst) - 1

    if min_index is None:
        return None

    return lst[min_index]

assert next_smallest([0, 1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([1, 1]) == None
assert next_smallest([0]) == None
assert next_smallest([0, 0]) == None
assert next_smallest([]) == None
