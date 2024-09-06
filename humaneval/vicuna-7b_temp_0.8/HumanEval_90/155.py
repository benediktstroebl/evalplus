
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
    i = 0
    while i < len(lst) - 1:
        if lst[i] < lst[i+1]:
            i += 1
        else:
            j = 0
            while j < i:
                if lst[j] > lst[i]:
                    i += 1
                    j += 1
            i = j
    return lst[i+1] if len(lst) > 0 else None
