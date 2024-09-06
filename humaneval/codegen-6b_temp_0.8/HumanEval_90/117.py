
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
    
    result = [False]
    def smaller(a, b):
        return a < b
    sort_list = sorted(lst)
    lst_len = len(lst) - 2
    while lst_len >= 0:
        if smaller(sort_list[lst_len], sort_list[lst_len + 1]):
            result.append(sort_list[lst_len + 1])
            break
        lst_len -= 1
    if not result:
        return None
    return result[1]
