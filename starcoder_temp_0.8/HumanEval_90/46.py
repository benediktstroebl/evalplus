
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
    # your code here
    if len(lst) < 2:
        return None
    min1, min2 = float('inf'), float('inf')
    for num in lst:
        if num < min1:
            min2 = min1
            min1 = num
        elif num > min1 and num < min2:
            min2 = num
    if min2 == float('inf'):
        return None
    return min2
