
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
    else:
        middle = lst[0]
        right = lst[1]
        left = middle + 1
        while left <= right:
            if left <= right:
                if left < right:
                    return left
                else:
                    return right
            middle = middle + 1
            left = middle
        return None
