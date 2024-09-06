
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
    left = 0
    right = len(lst) - 1
    smallest = lst[0]
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < smallest:
            smallest = lst[mid]
            left = mid + 1
        else:
            right = mid - 1
    return smallest
