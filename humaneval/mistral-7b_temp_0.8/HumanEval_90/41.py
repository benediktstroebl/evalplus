
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

    # Check if the list is empty
    if not lst:
        return None

    # Sort the list in ascending order
    sorted_lst = sorted(lst)

    # Get the second element of the sorted list
    second_smallest = sorted_lst[1] if len(sorted_lst) >= 2 else None

    return second_smallest
