
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
    min_num = float("inf")
    sec_min_num = float("inf")
    for num in lst:
        if num < min_num:
            sec_min_num = min_num
            min_num = num
        elif num < sec_min_num and num != min_num:
            sec_min_num = num
    if sec_min_num == float("inf"):
        return None
    return sec_min_num
