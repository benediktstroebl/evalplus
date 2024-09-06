
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
    # List to store integers
    int_list = []
    # List to store the tuple
    integer_tuple = []
    # Iterate through the list 'lst'
    for item in lst:
        # Check if integer and append to list
        if isinstance(item, int):
            int_list.append(item)
    # Check if the list 'int_list' is not empty
    if int_list:
        # Return the smallest positive integer
        integer_tuple.append(min(list(filter(lambda x: x >= 0, int_list))))
        # Return the largest negative integer
        integer_tuple.append(max(list(filter(lambda x: x < 0, int_list))))
    # If the list 'int_list' is empty
    else:
        # Return None for both
        integer_tuple.extend([None, None])
    return tuple(integer_tuple)
    
