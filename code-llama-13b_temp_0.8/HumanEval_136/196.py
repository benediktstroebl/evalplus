
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
    
    # Create list to store negative integers
    neg_ints = []
    # Create list to store positive integers
    pos_ints = []
    # Create a tuple to return
    return_tup = (None, None)
    # Loop through list of integers
    for i in lst:
        # Check if number is negative
        if i < 0:
            # Add number to neg_ints list
            neg_ints.append(i)
        # Check if number is positive
        elif i > 0:
            # Add number to pos_ints list
            pos_ints.append(i)
        # If number is neither positive or negative
        else:
            continue
    # Check if neg_ints is not empty
    if len(neg_ints) > 0:
        # Grab smallest negative integer
        largest_neg_int = min(neg_ints)
        # Update return_tup
        return_tup = (largest_neg_int, return_tup[1])
    # Check if pos_ints is not empty
    if len(pos_ints) > 0:
        # Grab largest positive integer
        smallest_pos_int = max(pos_ints)
        # Update return_tup
        return_tup = (return_tup[0], smallest_pos_int)
    return return_tup
    
    

