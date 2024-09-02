
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
    # Create an empty list that will store the desired indices of the list
    indices = []

    # Iterate over the list and add the indices of the elements to the list if they satisfy the condition
    for i in range(len(lst)):
        if lst[i] < lst[i+1]:
            indices.append(i)

    # If the list is empty, there is no second smallest element
    if not indices:
        return None

    # Return the second smallest element of the list using the indices that have been stored
    return lst[indices[1]]
