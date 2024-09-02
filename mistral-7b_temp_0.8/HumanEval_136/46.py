
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
    # TODO: Write your solution here
    pass
    # test cases
    test1 = largest_smallest_integers([2, 4, 1, 3, 5, 7])
    test2 = largest_smallest_integers([-2, -4, -1, -3, -5, -7])
    test3 = largest_smallest_integers([])
    test4 = largest_smallest_integers([0])
    assert test1 == (None, 1)
    assert test2 == (-7, -2)
    assert test3 == (None, None)
    assert test4 == (None, None)
    print("All test cases passed!")
