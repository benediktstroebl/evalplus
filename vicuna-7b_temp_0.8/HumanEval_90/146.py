
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
    left, right = 1, max(lst)
    while left < right:
        mid = (left + right) // 2
        if mid not in [left, right]:
            if mid < left[0]:
                left = mid
            elif mid < right[0]:
                right = mid
        elif left < mid[0]:
            left = mid
        else:
            right = mid
    return left if right == left else None