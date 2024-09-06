
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
    # print(lst)
    negative_numbers = [number for number in lst if number < 0]
    positive_numbers = [number for number in lst if number >= 0]
    # print(negative_numbers)
    # print(positive_numbers)
    if len(negative_numbers) == 0:
        largest_negative_number = None
    elif len(negative_numbers) == 1:
        largest_negative_number = negative_numbers[0]
    else:
        largest_negative_number = max(negative_numbers)

    if len(positive_numbers) == 0:
        smallest_positive_number = None
    elif len(positive_numbers) == 1:
        smallest_positive_number = positive_numbers[0]
    else:
        smallest_positive_number = min(positive_numbers)

    return largest_negative_number, smallest_positive_number

