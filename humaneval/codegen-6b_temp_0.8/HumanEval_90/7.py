
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
    if lst == []:
        return None
    
    temp = lst[:]
    temp.sort()
    return temp[1]
    
assert(next_smallest([1, 2, 3, 4, 5]) == 2)
assert(next_smallest([5, 1, 4, 3, 2]) == 2)
assert(next_smallest([]) == None)
assert(next_smallest([1, 1]) == None)
assert(next_smallest([1, 2, 3, 4, 5]) == 2)
assert(next_smallest([1, 2, 3, 4, 5, 5]) == 5)
assert(next_smallest([1, 2, 3, 4, 5, 3]) == 3)
assert(next_smallest([3, 1, 4, 5, 2]) == 1)
assert(next_smallest([3, 1, 4, 5, 2, 1]) == 1)
assert(next_smallest([2, 3, 1, 0, 0, 11, 22, 32]) == 0)

