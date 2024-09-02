
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

    else:
        new_list = []
        new_list2 = []
        for num in lst:
            if num >= 0:
                new_list2.append(num)
            if num < 0:
                new_list.append(num)
        new_list.sort()
        new_list2.sort()
        new_list.reverse()
        new_list2.reverse()
        return (new_list[0], new_list2[0])

