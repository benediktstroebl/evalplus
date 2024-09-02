
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
    negative_count = 0
    positive_count = 0
    for num in lst:
        if num < 0:
            negative_count += 1
        elif num > 0:
            positive_count += 1
    if negative_count == 0 and positive_count == 0:
        return None, None
    elif negative_count > 0 and positive_count == 0:
        return -1, lst[-1]
    elif negative_count == 0 and positive_count > 0:
        return lst[0], lst[-1]
    else:
        return lst[0], lst[-1]