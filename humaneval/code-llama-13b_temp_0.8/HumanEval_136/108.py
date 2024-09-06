
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

    # 1. Make a copy of the list
    new_lst = lst.copy()

    # 2. Sort the list in ascending order
    new_lst.sort()

    # 3. Check for negative integers, start from beginning
    negative_integer = None
    for x in new_lst:
        if x < 0:
            negative_integer = x
            break

    # 4. Check for positive integers, start from the end
    positive_integer = None
    for x in reversed(new_lst):
        if x > 0:
            positive_integer = x
            break

    return negative_integer, positive_integer
