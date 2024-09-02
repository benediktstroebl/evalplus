
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
    result_smallest = None
    result_largest = None
    for i in lst:
        if type(i) == int:
            if i < 0:
                if result_largest is not None:
                    if result_largest < i:
                        result_largest = i
                else:
                    result_largest = i
            elif i > 0:
                if result_smallest is not None:
                    if result_smallest > i:
                        result_smallest = i
                else:
                    result_smallest = i
    return (result_largest, result_smallest)
    

