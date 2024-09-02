
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
    # First, check if the list is empty
    if not lst:
        return (None, None)

    # If the list is not empty, check if it contains any positive or negative integers
    positive_or_negative = [int(x) for x in lst if x.isdigit() and x >= 0 or x < 0]
    if positive_or_negative:
        # If there are positive or negative integers, return their max and min values
        max_val = max(positive_or_negative)
        min_val = min(positive_or_negative)
        return max_val, min_val
    else:
        # If there are no positive or negative integers, return None for both values
        return (None, None)
