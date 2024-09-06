
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
    # your code here

    # List is empty
    if len(lst) == 0:
        return None
    # List has only one element
    if len(lst) == 1:
        return None
    # If second element is smaller than the first element
    elif lst[0] > lst[1]:
        return lst[1]
    else:
        # If the first element is the smallest
        if lst[0] == lst[1] or lst[0] < lst[1]:
            # If the list is sorted
            if lst[0] <= lst[1] <= lst[2]:
                return lst[2]
            # If the list has three elements and first element is smallest
            elif lst[0] < lst[1]:
                return lst[2]
            # If the list has three elements and first element is second smallest
            elif lst[0] > lst[1]:
                return lst[1]
        # If the second element is the smallest
        else:
            # If the list
