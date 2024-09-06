
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
    print("BEGIN TESTS")
    print("TEST 1")
    lst = [2, 4, 1, 3, 5, 7]
    res = (None, 1)
    if len(lst) == 0:
        print("TEST 1 FAILED")
        return None
    lst = [0]
    res = (None, None)
    if len(lst) == 0:
        print("TEST 2 FAILED")
        return None
    lst = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
    res = (-3, 0)
    if largest_smallest_integers(lst) != res:
        print("TEST 3 FAILED")
        print("FAILED OUTPUT:", largest_smallest_integers(lst))
        return None
    lst = [2, 4, 6, -1, 3, -5, 1000, 7]
    res = (-5, 2)
    if largest_smallest_integers(lst) != res:
        print("TEST 4 FAILED")
        print("FAILED OUTPUT:", largest_smallest_integers(lst))
        return None
    print("ALL TESTS PASSED")

