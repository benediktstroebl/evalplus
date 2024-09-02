
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
    #Your code here
    #Remember to return your results as a tuple!
    #When the list is empty, return (None, None)

    #raise NotImplementedError

    a = None
    b = None
    list_to_check = []
    for num in lst:
        if num < 0:
            list_to_check.append(num)
        else:
            list_to_check.append(num)
    if len(list_to_check) > 0:
        a = max(list_to_check)
        b = min(list_to_check)
    return (a, b)
