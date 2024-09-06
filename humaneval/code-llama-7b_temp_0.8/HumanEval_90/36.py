
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

    min_elems = []

    # Iterate through the list
    for i in range(len(lst)):

        # Push the smallest element into the list
        if len(min_elems) < 2:
            min_elems.append(lst[i])

        # If the current element is smaller than the smallest element in the list, remove it and add the smallest element
        if lst[i] <= min_elems[-1]:
            min_elems.pop()
            min_elems.append(lst[i])
    
    # If there are more than 2 elements in the list
    if len(min_elems) > 2:
        return min_elems[1]
    
    # If there are 2 or less elements in the list
    return None
