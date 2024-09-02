
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
    # Your code here
    smallest = None
    largest = None
    for number in lst:
        if number > 0:
            if largest is None:
                largest = number
            elif largest < number:
                largest = number
        elif number < 0:
            if smallest is None:
                smallest = number
            elif smallest > number:
                smallest = number
    return (largest, smallest)
