
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
    if lst is None or len(lst) == 0:
        return None

    current_min = float("inf")
    new_min = float("inf")

    for num in lst:
        if num < current_min:
            new_min = current_min
            current_min = num
        elif num < new_min and num != current_min:
            new_min = num

    if new_min == current_min:
        return None

    return new_min

