
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
    lst_count = 0
    largest = -sys.maxsize
    smallest = sys.maxsize
    for element in lst:
        if element < 0:
            lst_count += 1
            largest = max(largest, element)
        elif element > 0:
            lst_count += 1
            smallest = min(smallest, element)
    if lst_count == 0:
        return (None, None)
    elif lst_count == 1:
        return (largest, smallest)
    else:
        return (largest, smallest)
