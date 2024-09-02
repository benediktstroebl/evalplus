
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
    num1 = []
    num2 = []
    for x in lst:
        if x < 0:
            num1.append(x)
        elif x > 0:
            num2.append(x)
    if num1 == [] or num2 == []:
        return (None, None)
    else:
        return (max(num1), min(num2))

