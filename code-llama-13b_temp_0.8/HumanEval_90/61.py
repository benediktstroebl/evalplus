
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
    def get_smallest(lst):
        smallest = lst[0]
        for i in range(1, len(lst)):
            if lst[i] < smallest:
                smallest = lst[i]
        return smallest
    
    def get_second_smallest(lst, smallest):
        for i in range(0, len(lst)):
            if lst[i] < smallest and lst[i] != smallest:
                return lst[i]
        return None
    
    smallest = get_smallest(lst)
    if smallest:
        return get_second_smallest(lst, smallest)
    return None
