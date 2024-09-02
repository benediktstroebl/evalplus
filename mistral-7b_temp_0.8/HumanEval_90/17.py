
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
    lst_min = float("inf")
    lst_min2 = float("inf")
    for num in lst:
        if num < lst_min:
            lst_min2 = lst_min
            lst_min = num
        elif num < lst_min2 and num != lst_min:
            lst_min2 = num

    if lst_min2 == float("inf"):
        return None

    return lst_min2
