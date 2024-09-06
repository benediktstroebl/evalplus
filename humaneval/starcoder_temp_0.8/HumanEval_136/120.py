
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
    # list for the positive integers
    positive_numbers = []
    # list for the negative integers
    negative_numbers = []
    # iterate over the list
    for number in lst:
        if number > 0:
            # append the positive numbers into the list
            positive_numbers.append(number)
        elif number < 0:
            # append the negative numbers into the list
            negative_numbers.append(number)
    # if the negative list is empty, return None for the first value
    if len(negative_numbers) == 0:
        a = None
    # if the negative list has values, return the largest negative integer
    else:
        a = max(negative_numbers)
    # if the positive list is empty, return None for the second value
    if len(positive_numbers) == 0:
        b = None
    # if the positive list has values, return the smallest positive integer
    else:
        b = min(positive_numbers)
    return (a, b)
