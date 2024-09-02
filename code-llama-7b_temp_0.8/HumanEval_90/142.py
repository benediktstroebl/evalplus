
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

    if not lst:
        return None

    min_val = float('inf')

    for item in lst:
        if item < min_val:
            min_val = item

    min_vals = [min_val]

    for item in lst:
        if item != min_val and item < min(min_vals):
            min_vals.append(item)
    
    if len(min_vals) == 1:
        return None
    else:
        return sorted(min_vals)[1]

