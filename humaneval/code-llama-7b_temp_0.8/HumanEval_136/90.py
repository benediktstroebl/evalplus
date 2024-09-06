
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
    # 1. Get all the integers.
    # 2. Keep the integers in order.
    # 3. Get the largest negative integer and the smallest positive integer.
    # 4. Return those numbers in a tuple.

    # Get all the integers.
    integers = [item for item in lst if type(item) is int]

    if integers:

        # Keep the integers in order.
        integers.sort()

        # Get the largest negative integer and the smallest positive integer.
        neg_int = None if integers[0] < 0 else integers[0]
        pos_int = None if integers[-1] > 0 else integers[-1]

        return (neg_int, pos_int)
    else:
        return (None, None)


