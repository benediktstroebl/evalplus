
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
    if len(lst) == 0:
        return (None, None)
    else:
        res_largest = None
        res_smallest = None
        for num in lst:
            if num > 0:
                if res_smallest is None:
                    res_smallest = num
                elif num < res_smallest:
                    res_smallest = num
            elif num < 0:
                if res_largest is None:
                    res_largest = num
                elif num > res_largest:
                    res_largest = num
        return (res_largest, res_smallest)
