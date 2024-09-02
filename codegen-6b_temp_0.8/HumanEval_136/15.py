
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
    # Create an empty list to store positive/negative ints
    large = []
    small = []

    # Iterate over list
    for num in lst:
        # If it's a negative int
        if num < 0:
            # Check if it's in the large list
            if num in large:
                continue
            else:
                # Add it to the small list
                small.append(num)
        # Else if it's a positive int
        else:
            # Check if it's in the small list
            if num in small:
                continue
            else:
                # Add it to the large list
                large.append(num)

    # If the list is empty, return (None, None)
    if large == []:
        return (None, None)

    if small == []:
        return (large[0], None)

    # Return a tuple
    return (min(large), max(small))
