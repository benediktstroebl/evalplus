
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
    left = 1
    right = max(lst) + 1
    while left <= right:
        mid = (left + right) // 2
        if mid == left or mid == right:
            return mid
        elif lst[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return None