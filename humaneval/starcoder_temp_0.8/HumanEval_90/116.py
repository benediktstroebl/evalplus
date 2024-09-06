
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
    def _smallest(start, end):
        return sorted(lst[start: end + 1])[1]

    def _next_smallest(start, end):
        if start == end:
            return None
        if _smallest(start, end) < _smallest(start + 1, end):
            return _smallest(start, end)
        else:
            return _next_smallest(start + 1, end)

    return _next_smallest(0, len(lst) - 1)
