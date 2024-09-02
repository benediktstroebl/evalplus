
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

    min_value = lst[0]
    min_index = 0
    for i, val in enumerate(lst):
        if val < min_value:
            min_index = i
            min_value = val
    return min_value if min_value!= min_index else None

