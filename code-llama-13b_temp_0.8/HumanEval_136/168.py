
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
    if lst == []:
        return (None, None)
    for num in lst:
        if num >= 1:
            index_positive = lst.index(num)
            num1 = num
            break
        else:
            num1 = None
            index_positive = None
    for num in lst[::-1]:
        if num <= -1:
            index_negative = lst.index(num)
            num2 = num
            break
        else:
            num2 = None
            index_negative = None
    if index_negative is not None:
        lst_positive = lst[:index_negative]
        largest_neg_integer = lst[index_negative]
    else:
        lst_positive = lst
        largest_neg_integer = None
    if index_positive is not None:
        lst_negative = lst[index_positive:]
        smallest_pos_integer = lst[index_positive]
    else:
        lst_negative = lst
        smallest_pos_integer = None
    if lst_positive == [] and lst_negative == []:
        return (None, None)
    elif lst_positive == []:
        return (largest_neg_integer, None)
    elif lst_negative == []:
        return (None, smallest_pos_integer)
    else:
        return (largest_neg_integer, smallest_pos_integer)

