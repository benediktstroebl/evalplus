
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
    for i in range(len(lst) - 1):
        smallest = lst[i]
        smallest_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < smallest:
                smallest = lst[j]
                smallest_index = j
        lst[i], lst[smallest_index] = lst[smallest_index], lst[i]
    return None if lst[len(lst) - 1] == lst[len(lst) - 2] else lst[len(lst) - 2]
