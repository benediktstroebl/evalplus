
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
    def get_2nd_smallest_element(lst):
        n = len(lst)
        if n < 2:
            return None
        min_1 = min_2 = 2**32 - 1
        for i in lst:
            if i < min_1:
                min_1, min_2 = i, min_1
            elif i < min_2 and i != min_1:
                min_2 = i
        return min_2 if min_1 != min_2 else None
    lst_sort = sorted(lst)
    return get_2nd_smallest_element(lst_sort)
