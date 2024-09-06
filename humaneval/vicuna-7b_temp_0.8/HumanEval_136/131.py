
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
    if not lst:
        return (None, None)

    negative_count = 0
    positive_count = 0
    for i in lst:
        if i < 0:
            negative_count += 1
            lst.remove(i)
        else:
            positive_count += 1

    if negative_count == 0 and positive_count == 0:
        return (None, None)

    largest = lst[0]
    smallest = lst[0]
    for i in lst[1:]:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i

    return (largest, smallest)