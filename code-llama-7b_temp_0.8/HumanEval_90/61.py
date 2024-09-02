
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
    # sort the list
    lst.sort()

    # get the index of the smallest element
    min_index = lst.index(min(lst))

    # if the smallest element is the last element, return None
    if min_index == len(lst) - 1:
        return None
    # return the next smallest
    else:
        return lst[min_index + 1]

