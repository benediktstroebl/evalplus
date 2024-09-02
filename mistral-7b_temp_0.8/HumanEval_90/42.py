
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
    # create an empty list to hold the sorted values of the original list
    sorted_lst = []

    # sort the original list
    sorted_lst = sorted(lst)

    # if the length of the original list is less than 2, return None
    if len(sorted_lst) < 2:
        return None

    # if the second element in the sorted list is less than the first element,
    # return the first element
    if sorted_lst[1] < sorted_lst[0]:
        return sorted_lst[1]
    # otherwise, return None
    else:
        return None
