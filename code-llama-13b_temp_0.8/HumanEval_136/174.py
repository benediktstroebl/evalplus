
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
    if lst == []:
        return (None, None)
    
    sorted_list = sorted(lst)
    smallest_positive = sorted_list[0] if sorted_list[0] > 0 else None
    largest_negative = sorted_list[-1] if sorted_list[-1] < 0 else None
    return (largest_negative, smallest_positive)

