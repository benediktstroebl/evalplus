
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
    # smallest = None
    # largest = None
    #
    # for elem in lst:
    #     if largest is None or elem > largest:
    #         largest = elem
    #
    #     if smallest is None or elem < smallest:
    #         smallest = elem
    #
    # return smallest, largest

    # lst.sort()
    # if lst[0] < 0:
    #     return lst[0], lst[-1]
    # elif lst[0] > 0:
    #     return None, None

    lst.sort()

    return (lst[0] if lst[0] < 0 else None, lst[-1] if lst[-1] > 0 else None)
