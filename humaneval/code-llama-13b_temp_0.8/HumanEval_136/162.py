
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
    # create a list to store only integers
    numbers = []
    for i in lst:
        if type(i) == int:
            numbers.append(i)

    # if there are no numbers in the list, return None
    if len(numbers) == 0:
        return (None, None)

    # if there are no negative numbers, return None
    smallest_positive = min(numbers)
    if smallest_positive >= 0:
        return (None, smallest_positive)

    # if there are no positive numbers, return None
    largest_negative = max(numbers)
    if largest_negative <= 0:
        return (largest_negative, None)

    # return the tuple
    return (largest_negative, smallest_positive)

