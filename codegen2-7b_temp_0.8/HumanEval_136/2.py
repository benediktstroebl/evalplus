
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
    negative_numbers = []
    positive_numbers = []

    for n in lst:
        if n < 0:
            negative_numbers.append(n)
        else:
            positive_numbers.append(n)

    if len(negative_numbers) > 0:
        largest_negative_number = max(negative_numbers)
    else:
        largest_negative_number = None

    if len(positive_numbers) > 0:
        smallest_positive_number = min(positive_numbers)
    else:
        smallest_positive_number = None

    return largest_negative_number, smallest_positive_
