
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
    integer_lst = []
    for i in lst:
        if type(i) == int:
            integer_lst.append(i)
        else:
            return (None, None)

    if not integer_lst:
        return (None, None)

    integer_lst = sorted(integer_lst)
    largest = None
    smallest = None

    if integer_lst[0] < 0:
        largest = integer_lst[0]
        for i in integer_lst:
            if i < 0:
                if i > largest:
                    largest = i
            else:
                break

    if integer_lst[-1] > 0:
        smallest = integer_lst[-1]
        for i in integer_lst[::-1]:
            if i > 0:
                if i < smallest:
                    smallest = i
            else:
                break
    return (largest, smallest)

