
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
    # Remove the items that are equal to 0.
    lst = list(filter(lambda x: x != 0, lst))
    # Check if the list is empty.
    if not lst:
        return (None, None)
    # Determine the max and min of the list.
    max_of_negative = min(lst)
    min_of_positive = max(lst)
    # Return a tuple containing the max and min
    return (max_of_negative, min_of_positive)
