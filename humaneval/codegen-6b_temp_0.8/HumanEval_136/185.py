
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
    negative_ints = [int(num) for num in lst if num < 0]
    positive_ints = [int(num) for num in lst if num > 0]
    if not positive_ints:
        return None, None
    elif not negative_ints:
        return None, max(positive_ints)
    else:
        return max(negative_ints), min(positive_ints)
