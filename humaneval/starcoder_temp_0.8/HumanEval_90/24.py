
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
    
    smallest_idx = 0
    smallest_elem = lst[0]

    for idx, elem in enumerate(lst):
        if elem < smallest_elem:
            smallest_elem = elem
            smallest_idx = idx

    if smallest_idx > 0 and lst[smallest_idx - 1]!= smallest_elem:
        return lst[smallest_idx - 1]
    elif smallest_idx < len(lst) - 1 and lst[smallest_idx + 1]!= smallest_elem:
        return lst[smallest_idx + 1]
    else:
        return None
