
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
    # This is the function I came up with, but I'm not sure if it's correct.
    # The problem is that I'm not sure how to check if there is a negative or
    # positive integer in the list, or if the list is empty
    if len(lst) == 0:
        return (None, None)
    elif not any(lst):
        return (None, None)
    elif not any(-lst for lst in reversed(lst)):
        return (None, None)
    elif not any([int(x) > 0 for x in lst]):
        return (None, lst[0])
    elif not any([int(x) < 0 for x in lst]):
        return (lst[-1], None)
    elif not any([int(x) > 0 for x in lst] or int(lst[0]) > 0):
        return (lst[0], lst[-1])
    else:
        return (lst[0], lst[-1])