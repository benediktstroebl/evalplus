
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
    def get_largest_and_smallest(lst):
        if not lst:
            return None, None

        largest = min(lst)
        lowest = max(lst)
        return largest, lowest

    largest, lowest = get_largest_and_smallest(lst)

    lst.remove(largest)
    if not lst:
        return None, None

    next_largest, next_lowest = get_largest_and_smallest(lst)

    if next_largest is not None:
        return (largest, next_lowest)
    else:
        return (largest, lowest)

