
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
    # Your code here
    if lst == []:
        return None

    def find_smallest(lst, smallest):
        if lst[0] == smallest:
            return find_smallest(lst[1:], lst[1])
        else:
            return find_smallest(lst[1:], lst[0])
    
    smallest = find_smallest(lst, lst[0])
    
    for i in range(len(lst)):
        if lst[i] == smallest:
            return lst[i+1]
    
    return None












