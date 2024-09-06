
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
    if len(lst) <= 1:
        return None
    min1, min2 = 0, 1
    for i in range(len(lst)):
        if lst[min1] > lst[i]:
            min2 = min1
            min1 = i
        elif lst[min2] > lst[i] and lst[i]!= lst[min1]:
            min2 = i
    if min1!= min2:
        return lst[min2]
    else:
        return None

