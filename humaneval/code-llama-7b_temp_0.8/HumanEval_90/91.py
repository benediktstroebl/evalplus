
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
    # this is the solution i came up with while following the problems instructions.
    # we want to find the first smallest element, if we find it we remove it, if not we return none.
    # if we find a smaller element, we add it to the front of the list, and return the 2nd smallest element
    # we then iterate over the rest of the list, and either return the 2nd smallest element or none
    # if we find an element that is less than the 2nd smallest we replace the 2nd smallest and iterate again
    def find_first(lst):
        if not lst:
            return None
        first = lst.pop(0)
        while lst:
            if lst.pop(0) < first:
                first = lst.pop(0)
                if lst:
                    first = lst.pop(0)
        return first

    if not lst:
        return None

    first = find_first(lst)
    if not first:
        return None
    if not lst:
        return None
    second = lst.pop(0)
    if second < first:
        return second
    if not lst:
        return None
    second_lst = [second] + lst
    second = find_first(second_lst)
    if not second:
        return None
    for item in lst:
        if item < second:
            second = item
    return second
