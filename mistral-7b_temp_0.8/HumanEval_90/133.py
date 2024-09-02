
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
    if len(lst) == 2:
        if lst[0] < lst[1]:
            return lst[0]
        else:
            return lst[1]
    mid = len(lst)//2
    left_smaller = lst[:mid]
    right_smaller = lst[mid + 1:]
    if len(right_smaller) == 0:
        return lst[mid]
    elif len(right_smaller) == 1:
        return lst[mid] if lst[mid] < lst[mid + 1] else lst[mid + 1]
    else:
        left_smallest = left_smaller[0]
        right_smallest = right_smaller[0]
        if lst[mid] < left_smallest:
            return lst[mid]
        else:
            return next_smallest(right_smaller)

