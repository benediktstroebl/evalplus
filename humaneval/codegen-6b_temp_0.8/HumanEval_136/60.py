
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
    largest = None
    smallest = None
    for num in lst:
        if num > smallest and num < largest:
            smallest = num
        elif num < smallest and num > largest:
            largest = num

    return (largest, smallest)

assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (1, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([1]) == (None, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7]) == (None, 1)
