
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
    list_of_positive_numbers = []
    list_of_negative_numbers = []
    for i in lst:
        if i > 0:
            list_of_positive_numbers.append(i)
        if i < 0:
            list_of_negative_numbers.append(i)
    if len(list_of_positive_numbers) == 0:
        return None, None
    if len(list_of_negative_numbers) == 0:
        return None, None
    largest_positive = max(list_of_positive_numbers)
    smallest_negative = min(list_of_negative_numbers)
    return largest_positive, smallest_negative
