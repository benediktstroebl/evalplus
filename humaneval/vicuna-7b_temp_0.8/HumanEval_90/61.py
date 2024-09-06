
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
    # 1. Find the smallest element of the list
    min_index = 0
    min_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_index = i
            min_val = lst[i]
    # 2. Find the index of the smallest element
    index = min_index
    smallest_val = lst[index]
    # 3. Find the index of the second smallest element
    for i in range(index + 1, len(lst)):
        if lst[i] < smallest_val:
            smallest_val = lst[i]
            index = i
    # 4. Return the second smallest element or None if there is no such element
    return smallest_val