
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
    high = len(lst) - 1
    low = 0
    mid = 0
    while low <= high:
        mid = (high - low) / 2 + low
        if lst[mid] > lst[high]:
            low = mid + 1
        elif lst[mid] < lst[high]:
            high = mid
        else:
            high = high - 1
    if low > len(lst) - 2:
        return None
    return lst[low + 1]
