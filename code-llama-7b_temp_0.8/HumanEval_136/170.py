
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    # Check if the list is empty
    if lst == []:
        return None, None
    
    # Set initial values to the first element
    smallest_positive = lst[0]
    largest_negative = lst[0]
    
    # Iterate through the list
    for num in lst:
        # If the number is positive
        if num > 0:
            # And it's smaller than the smallest positive
            if smallest_positive > num:
                smallest_positive = num
        # If the number is negative
        if num < 0:
            # And it's larger than the largest negative
            if largest_negative < num:
                largest_negative = num
    return largest_negative, smallest_positive
