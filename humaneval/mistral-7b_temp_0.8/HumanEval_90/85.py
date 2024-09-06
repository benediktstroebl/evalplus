
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

    # Create an empty list to store the next smallest element
    next_smaller = []
    # Loop through the list
    for element in lst:
        # Check if the current element is smaller than the previous elements
        if element < lst[i - 1] and element < lst[i + 1]:
            # If the current element is smaller than the previous elements, add it to the next_smaller list
            next_smaller.append(element)
    # Return the second element of the next_smaller list, or None if the list is empty
    return next_smaller[1] if next_smaller else None
