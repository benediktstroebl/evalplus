
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
    for i in lst:
        if i < 0:
            negative_count += 1
        else:
            positive_count += 1

    if negative_count > positive_count:
        return (-lst[0], lst[negative_count])
    elif positive_count > negative_count:
        return (lst[0], lst[positive_count])
    else:
        return (None, None)